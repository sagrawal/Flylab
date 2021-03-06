#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('calibration')
import rospy
import cv
import numpy as N
import tf
from cv_bridge import CvBridge, CvBridgeError
from pythonmodules import cvNumpy,CameraParameters
from sensor_msgs.msg import Image, CameraInfo
from geometry_msgs.msg import PoseStamped
from plate_tf.srv import *
from tracking.msg import ContourInfo
from patterngen.msg import MsgPattern
from flycore.msg import MsgFrameState


class CalibrateStagePlate():
    def __init__(self):
        self.initialized = False
        self.initialized_images = False
        self.initialized_pose = False
        self.initialized_arrays = False
        self.initialized_endeffector = False
        
        rospy.init_node('CalibrateStagePlate')
        
        self.camerainfo = None
        self.rvec = None
        self.tvec = None
        self.subCameraInfo = rospy.Subscriber("camera/camera_info", CameraInfo, self.CameraInfo_callback)
        self.subImage = rospy.Subscriber("camera/image_rect", Image, self.image_callback)
        self.subContourInfo = rospy.Subscriber("ContourInfo", ContourInfo, self.contourinfo_callback)
        self.subEndEffector = rospy.Subscriber('EndEffector', MsgFrameState, self.EndEffector_callback)
        self.pubPatternGen = rospy.Publisher('SetSignalGen', MsgPattern, latch=True)
        
        self.tf_listener = tf.TransformListener()

        cv.NamedWindow("Stage Plate Calibration", 1)
        
        self.poseRobot_camera = PoseStamped()
        self.poseRobot_rect = PoseStamped()
        self.poseRobot_plate = PoseStamped()
        
        rospy.on_shutdown(self.OnShutdown_callback)

        self.cvbridge = CvBridge()
        self.color_max = 255
        self.font = cv.InitFont(cv.CV_FONT_HERSHEY_TRIPLEX,0.5,0.5)
        self.font_color = cv.CV_RGB(self.color_max,0,0)
        
        #self.sample_dist_min = 10
        
        self.point_count_min = 60
        self.dist_min = 10
        
        self.error_text = ""
        self.eccRobot = 0
        self.areaRobot = 0
        self.eccRobot_array = N.array([])
        self.areaRobot_array = N.array([])
        self.eccRobotMin = 1000000000
        self.eccRobotMax = 0
        self.areaRobotMin = 1000000000
        self.areaRobotMax = 0
        
        # self.plate_point_array = N.zeros((1,3))
        # self.stage_point_array = N.zeros((1,3))
        #(self.intrinsic_matrix,self.distortion_coeffs) = CameraParameters.intrinsic("rect")
        self.origin_points = cv.CreateMat(4, 3, cv.CV_32FC1)
        self.origin_points_projected = cv.CreateMat(4,2,cv.CV_32FC1)
        self.checker_size = 15
        self.num_grid_lines = 9
        self.start_points_projected = cv.CreateMat(self.num_grid_lines,2,cv.CV_32FC1)
        self.end_points_projected = cv.CreateMat(self.num_grid_lines,2,cv.CV_32FC1)
        self.rotate_grid = False
        
        got_trans = False
        while not got_trans:
            try:
                (self.camera_rect_trans,rot) = self.tf_listener.lookupTransform('/ImageRect', '/Camera', rospy.Time(0))
                got_trans = True
            except:
                rospy.logdebug("tf_listener.lookupTransform threw exception \n")
        
        rospy.wait_for_service('plate_from_camera')
        try:
            self.plate_from_camera = rospy.ServiceProxy('plate_from_camera', PlateCameraConversion)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
        
        
    def OnShutdown_callback(self):
        if self.initialized:
            msgPattern = MsgPattern()
            msgPattern.mode = 'byshape'
            msgPattern.shape = 'constant'
            msgPattern.points = []
            msgPattern.frame = 'Stage'
            msgPattern.hzPattern = 1.0
            msgPattern.hzPoint = 100
            msgPattern.count = 1
            msgPattern.radius = 0.0
            msgPattern.preempt = True
            self.pubPatternGen.publish (msgPattern)
        
    
    def EndEffector_callback (self, state):
        self.initialized_endeffector = True
        
    
    def CameraInfo_callback (self, msgCameraInfo):
        if self.camerainfo is None:
            self.camerainfo = msgCameraInfo
            self.M = N.reshape(N.array(self.camerainfo.K),[3,3])
            # Makes with respect to Camera coordinate system instead of ImageRect
            self.M[:-1,-1] = 0

            (self.rvec, self.tvec) = CameraParameters.extrinsic("plate")
      
      
        
    def initialize_images(self,cv_image):
        self.im_size = cv.GetSize(cv_image)
        (self.im_width, self.im_height) = cv.GetSize(cv_image)
        # self.im = cv.CreateImage(self.im_size,cv.IPL_DEPTH_8U,1)
        self.im_display = cv.CreateImage(self.im_size,cv.IPL_DEPTH_8U,3)
        cv.Zero(self.im_display)
        self.initialized_images = True
    
    
    def draw_origin(self,im_color):
        if self.camerainfo is not None:
            cv.SetZero(self.origin_points)
            cv.SetReal2D(self.origin_points,1,0,self.checker_size) # x-direction
            cv.SetReal2D(self.origin_points,2,1,self.checker_size) # y-direction
            cv.SetReal2D(self.origin_points,3,2,self.checker_size) # z-direction
            axis_line_width = 3
            rect_line_width = 2
            cvmatK = cv.fromarray(N.reshape(self.camerainfo.K,[3,3]))
            cvmatD = cv.fromarray(N.reshape(self.camerainfo.D,[5,1]))
            cv.ProjectPoints2(self.origin_points,
                              self.rvec,
                              self.tvec,
                              cvmatK,
                              cvmatD,
                              self.origin_points_projected)
            
            try:
                a = cvNumpy.mat_to_array(self.origin_points_projected)
                
                # origin point
                pt1 = tuple(a[0])
                
                # draw x-axis
                pt2 = tuple(a[1])
                cv.Line(im_color,pt1,pt2,cv.CV_RGB(self.color_max,0,0),axis_line_width)
                
                # draw y-axis
                pt2 = tuple(a[2])
                cv.Line(im_color,pt1,pt2,cv.CV_RGB(0,self.color_max,0),axis_line_width)
                
                # draw z-axis
                pt2 = tuple(a[3])
                cv.Line(im_color,pt1,pt2,cv.CV_RGB(0,0,self.color_max),axis_line_width)
                
                # if self.image_plate_origin_found:
                #   self.image_plate_origin = pt1
                #   self.image_plate_origin_found = False
                
                # display_text = "image_plate_origin = " + str(self.image_plate_origin)
                # cv.PutText(self.im_display,display_text,(25,85),self.font,self.font_color)
                # display_text = "image_plate_origin = (%0.0f, %0.0f)" % (self.image_plate_origin[0],self.image_plate_origin[1])
                # cv.PutText(self.im_display,display_text,(25,85),self.font,self.font_color)
            except:
                pass
            

    def to_homo(self,array):
        array = N.append(array, N.ones((1, array.shape[1])), axis=0)
        return array
    
    
    def from_homo(self,array):
        return array[:-1,:]
    
    
    def draw_grid(self, im_color):
        if self.camerainfo is not None:
            points_range = (N.array(range(self.num_grid_lines)) - (self.num_grid_lines-1)/2) * self.checker_size
            points_zeros = N.zeros(points_range.shape)
            points_ones = N.ones(points_range.shape) * self.checker_size * (self.num_grid_lines - 1)/2
            
            x_start_points_array = N.array([-points_ones, points_range, points_zeros]).astype('float32')
            x_end_points_array = N.array([points_ones, points_range, points_zeros]).astype('float32')
            
            y_start_points_array = N.array([points_range, -points_ones, points_zeros]).astype('float32')
            y_end_points_array = N.array([points_range, points_ones, points_zeros]).astype('float32')
            
            
            if self.rotate_grid:
                x_start_points_array = self.from_homo(N.dot(self.T_stage_plate,self.to_homo(x_start_points_array)))
                x_end_points_array = self.from_homo(N.dot(self.T_stage_plate,self.to_homo(x_end_points_array)))
                y_start_points_array = self.from_homo(N.dot(self.T_stage_plate,self.to_homo(y_start_points_array)))
                y_end_points_array = self.from_homo(N.dot(self.T_stage_plate,self.to_homo(y_end_points_array)))
                self.rotate_grid = False
            
            x_start_points = cvNumpy.array_to_mat(x_start_points_array.transpose())
            x_end_points = cvNumpy.array_to_mat(x_end_points_array.transpose())
            y_start_points = cvNumpy.array_to_mat(y_start_points_array.transpose())
            y_end_points = cvNumpy.array_to_mat(y_end_points_array.transpose())
            
            axis_line_width = 1
            
            cvmatK = cv.fromarray(N.reshape(self.camerainfo.K,[3,3]))
            cvmatD = cv.fromarray(N.reshape(self.camerainfo.D,[5,1]))
            cv.ProjectPoints2(x_start_points,
                              self.rvec,
                              self.tvec,
                              cvmatK,
                              cvmatD,
                              self.start_points_projected)
            cv.ProjectPoints2(x_end_points,
                              self.rvec,
                              self.tvec,
                              cvmatK,
                              cvmatD,
                              self.end_points_projected)
            
            start_points = cvNumpy.mat_to_array(self.start_points_projected)
            end_points = cvNumpy.mat_to_array(self.end_points_projected)
            
            for line_n in range(self.num_grid_lines):
                cv.Line(im_color, tuple(start_points[line_n,:]), tuple(end_points[line_n,:]), cv.CV_RGB(self.color_max,0,0), axis_line_width)
            
            cv.ProjectPoints2(y_start_points,
                              self.rvec,
                              self.tvec,
                              cvmatK,
                              cvmatD,
                              self.start_points_projected)
            cv.ProjectPoints2(y_end_points,
                              self.rvec,
                              self.tvec,
                              cvmatK,
                              cvmatD,
                              self.end_points_projected)
            
            start_points = cvNumpy.mat_to_array(self.start_points_projected)
            end_points = cvNumpy.mat_to_array(self.end_points_projected)
            
            for line_n in range(self.num_grid_lines):
                cv.Line(im_color, tuple(start_points[line_n,:]), tuple(end_points[line_n,:]), cv.CV_RGB(0,self.color_max,0), axis_line_width)
            

    def image_callback(self, image):
        if self.initialized:
            try:
                cv_image = cv.GetImage(self.cvbridge.imgmsg_to_cv(image, "passthrough"))
            except CvBridgeError, e:
                print e
            
            if not self.initialized_images:
                self.initialize_images(cv_image)
            
            cv.CvtColor(cv_image, self.im_display, cv.CV_GRAY2RGB)
            y = 25
            
            
            if self.initialized_pose:
                try:
                    (trans,rot_quat) = self.tf_listener.lookupTransform('Stage', 'EndEffector', rospy.Time(0))
                    xEndEffector = trans[0]
                    yEndEffector = trans[1]
                    zEndEffector = trans[2]
                    
                    if self.initialized_arrays:
                        image_point_num = self.image_point_array.shape[1]
                        for image_point_n in range(image_point_num):
                            cv.Circle(self.im_display, (int(self.image_point_array[0,image_point_n]),int(self.image_point_array[1,image_point_n])), 5, cv.CV_RGB(self.color_max,0,self.color_max), cv.CV_FILLED)
                    
                    cv.Circle(self.im_display, (int(self.poseRobot_rect.pose.position.x),int(self.poseRobot_rect.pose.position.y)), 3, cv.CV_RGB(0,0,self.color_max), cv.CV_FILLED)
                    # display_text = "poseRobot_camera.x = " + str(round(self.poseRobot_camera.pose.position.x,3))
                    # cv.PutText(self.im_display,display_text,(25,25),self.font,self.font_color)
                    # display_text = "poseRobot_camera.y = " + str(round(self.poseRobot_camera.pose.position.y,3))
                    # cv.PutText(self.im_display,display_text,(25,45),self.font,self.font_color)
                    
                    display_text = "RobotImage Pose with Respect to Plate = [%0.3f, %0.3f]" % (self.poseRobot_plate.pose.position.x,self.poseRobot_plate.pose.position.y)
                    cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                    y = y+20
                    
                    # display_text = "poseRobot_plate.x = " + str(round(self.poseRobot_plate.pose.position.x,3))
                    # cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                    #y = y+20
                    # display_text = "poseRobot_plate.y = " + str(round(self.poseRobot_plate.pose.position.y,3))
                    # cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                    #y = y+20
                    
                    display_text = "EndEffector Pose with Respect to Stage = [%0.3f, %0.3f]" % (xEndEffector, yEndEffector)
                    cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                    y = y+20
                    
                    # display_text = "stage_state.x = " + str(round(self.stage_state.x,3))
                    # cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                    #y = y+20
                    # display_text = "stage_state.y = " + str(round(self.stage_state.y,3))
                    # cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                    #y = y+20
                    
                    image_point_new = N.array([[self.poseRobot_rect.pose.position.x], [self.poseRobot_rect.pose.position.y]])
                    plate_point_new = N.array([[self.poseRobot_plate.pose.position.x], [self.poseRobot_plate.pose.position.y],[0]])
                    stage_point_new = N.array([[xEndEffector], [yEndEffector], [zEndEffector]])
                    # rospy.logwarn("plate_point_new = \n%s", str(plate_point_new))
                    # rospy.logwarn("stage_point_new = \n%s", str(stage_point_new))
                    
                    if self.initialized_arrays:
                        plate_point_prev = self.plate_point_array[:,-1].reshape((3,1))
                        # rospy.logwarn("plate_point_prev = \n%s", str(plate_point_prev))
                        if self.dist_min < tf.transformations.vector_norm((plate_point_new - plate_point_prev)):
                            self.image_point_array = N.append(self.image_point_array,image_point_new,axis=1)
                            self.plate_point_array = N.append(self.plate_point_array,plate_point_new,axis=1)
                            # rospy.logwarn("plate_point_array = \n%s", str(self.plate_point_array))
                            self.stage_point_array = N.append(self.stage_point_array,stage_point_new,axis=1)
                            # rospy.logwarn("stage_point_array = \n%s", str(self.stage_point_array))
                            self.eccRobot_array = N.append(self.eccRobot_array,self.eccRobot)
                            self.areaRobot_array = N.append(self.areaRobot_array,self.areaRobot)
                    else:
                        self.image_point_array = image_point_new
                        self.plate_point_array = plate_point_new
                        self.stage_point_array = stage_point_new
                        self.initialized_arrays = True
                    
                    if self.point_count_min < self.plate_point_array.shape[1]:
                        self.T_plate_stage = tf.transformations.superimposition_matrix(self.plate_point_array, self.stage_point_array, scaling=True)
                        self.T_stage_plate = tf.transformations.inverse_matrix(self.T_plate_stage)
                        # self.T_stage_plate = tf.transformations.superimposition_matrix(self.plate_point_array, self.stage_point_array)
                        # self.T_plate_stage = tf.transformations.inverse_matrix(self.T_stage_plate)
                        # tvector = tf.transformations.translation_from_matrix(self.T_plate_stage)
                        tvector = tf.transformations.translation_from_matrix(self.T_stage_plate)
                        display_text = "Translation Vector = [%0.3f, %0.3f, %0.3f]" % (tvector[0],tvector[1],tvector[2])
                        cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                        y = y+20
                        # rospy.logwarn("tvec = \n%s",str(tvec))
                        # quaternion = tf.transformations.quaternion_from_matrix(self.T_plate_stage)
                        quaternion = tf.transformations.quaternion_from_matrix(self.T_stage_plate)
                        display_text = "Quaternion = [%0.3f, %0.3f, %0.3f, %0.3f]" % (quaternion[0],quaternion[1],quaternion[2],quaternion[3])
                        cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                        y = y+20
                        # rospy.logwarn("quaternion = \n%s",str(quaternion))
                        # euler = tf.transformations.euler_from_matrix(self.T_plate_stage,'rxyz')
                        # display_text = "Translation Vector = [%0.2f, %0.2f, %0.2f]" % (self.tvec[0],
                        # cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                        #y = y+20
                        # rospy.logwarn("euler = \n%s",str(euler))
                        
                        eccMean = N.mean(self.eccRobot_array)
                        eccStd = N.std(self.eccRobot_array)
                        # rospy.logwarn("eccMean = %s, eccStd = %s\n" % (eccMean, eccStd))
                        self.eccRobotMin = eccMean - eccStd*3
                        if self.eccRobotMin < 0:
                            self.eccRobotMin = 0
                        self.eccRobotMax = eccMean + eccStd*3
                        areaMean = N.mean(self.areaRobot_array)
                        areaStd = N.std(self.areaRobot_array)
                        # rospy.logwarn("areaMean = %s, areaStd = %s\n" % (areaMean, areaStd))
                        self.areaRobotMin = areaMean - areaStd*3
                        if self.areaRobotMin < 0:
                            self.areaRobotMin = 0
                        self.areaRobotMax = areaMean + areaStd*3
                        display_text = "eccRobotMin = %0.3f, eccRobotMax = %0.3f" % (self.eccRobotMin, self.eccRobotMax)
                        cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                        y = y+20
                        display_text = "areaRobotMin = %0.0f, areaRobotMax = %0.0f" % (self.areaRobotMin, self.areaRobotMax)
                        cv.PutText(self.im_display,display_text,(25,y),self.font,self.font_color)
                        y = y+20
                        
                        factor, origin, direction = tf.transformations.scale_from_matrix(self.T_stage_plate)
                        display_text = "Factor = %s" % factor
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        display_text = "Origin = %s" % origin
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        display_text = "Direction = %s" % direction
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        display_text = "T_stage_plate = %s" % self.T_stage_plate[0]
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        display_text = "T_stage_plate = %s" % self.T_stage_plate[1]
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        display_text = "T_stage_plate = %s" % self.T_stage_plate[2]
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        display_text = "T_stage_plate = %s" % self.T_stage_plate[3]
                        cv.PutText(self.im_display, display_text, (25,y), self.font, self.font_color)
                        y = y+20
                        
                        self.rotate_grid = True
                        self.draw_grid(self.im_display)
                    
                        self.draw_origin(self.im_display)
                        self.draw_grid(self.im_display)
                        
                except (tf.LookupException, tf.ConnectivityException):
                    pass
            
            
            cv.PutText(self.im_display, self.error_text, (25,y), self.font, self.font_color)
            
            cv.ShowImage("Stage Plate Calibration", self.im_display)
            cv.WaitKey(3)

    # def cbPose(self,contourinfo):
    #   if not self.initialized_pose:
    #     self.initialized_pose = True
    #   self.poseRobot_camera.header = contourinfo.header
    #   self.poseRobot_camera.pose.position.x = contourinfo.pose.position.x
    #   self.poseRobot_camera.pose.position.y = contourinfo.pose.position.y
    #   self.poseRobot_rect = self.camera_to_rect_pose(self.poseRobot_camera)
    #   self.poseRobot_plate = self.PosePlateFromCamera(self.poseRobot_camera)
    
    def contourinfo_callback(self,contourinfo):
        if self.initialized:
            header = contourinfo.header
            x_list = contourinfo.x
            y_list = contourinfo.y
            angle_list = contourinfo.angle
            area_list = contourinfo.area
            ecc_list = contourinfo.ecc
            contour_count = min(len(x_list),len(y_list),len(angle_list),len(area_list),len(ecc_list))
            
            if contour_count == 1:
                self.error_text = ""
                if not self.initialized_pose:
                    self.initialized_pose = True
                  
                self.poseRobot_camera.header = contourinfo.header
                self.poseRobot_camera.pose.position.x = x_list[0]
                self.poseRobot_camera.pose.position.y = y_list[0]
                self.poseRobot_rect = self.camera_to_rect_pose(self.poseRobot_camera)
                self.poseRobot_plate = self.PosePlateFromCamera(self.poseRobot_camera)
                self.areaRobot = area_list[0]
                self.eccRobot = ecc_list[0]
            else:
                rospy.logwarn("Error! More than one object detected!")
                self.error_text = "Error! More than one object detected!"
            
            # for contour in range(contour_count):
            #   x = x_list[contour]
            #   y = y_list[contour]
            #   angle = angle_list[contour]
            #   area = area_list[contour]
            #   ecc = ecc_list[contour]
            #   # Identify robot
            #   if ((self.areaRobotMin < area) and (area < self.areaRobotMax)) and ((self.eccRobotMin < ecc) and (ecc < self.eccRobotMax)):
            #     self.poseRobot.header = header
            #     self.poseRobot.pose.position.x = x
            #     self.poseRobot.pose.position.y = y
            #     self.poseRobot_pub.publish(self.poseRobot)
            #   elif contour_count == 2:
            #     self.fly_image_pose.header = header
            #     self.fly_image_pose.pose.position.x = x
            #     self.fly_image_pose.pose.position.y = y
            #     self.fly_image_pose_pub.publish(self.fly_image_pose)

    def camera_to_rect_pose(self,poseCamera):
        poseRect = PoseStamped()
        poseRect.pose.position.x = self.camera_rect_trans[0] + poseCamera.pose.position.x
        # rospy.logwarn("poseCamera.pose.position.x \n%s",str(poseCamera.pose.position.x))
        # rospy.logwarn("self.camera_rect_trans[0] \n%s",str(self.camera_rect_trans[0]))
        # rospy.logwarn("self.poseRect.pose.position.x \n%s",str(poseRect.pose.position.x))
        poseRect.pose.position.y = self.camera_rect_trans[1] + poseCamera.pose.position.y
        # rospy.logwarn("poseCamera.pose.position.y \n%s",str(poseCamera.pose.position.y))
        # rospy.logwarn("self.camera_rect_trans[1] \n%s",str(self.camera_rect_trans[1]))
        # rospy.logwarn("self.poseRect.pose.position.y \n%s",str(poseRect.pose.position.y))
        return poseRect
    
    
    def PosePlateFromCamera(self, poseCamera):
        response = self.plate_from_camera([poseCamera.pose.position.x],[poseCamera.pose.position.y])
        # rospy.logwarn("Xdst \n%s",str(response.Xdst))
        # rospy.logwarn("Ydst \n%s",str(response.Ydst))
        posePlate = PoseStamped()
        posePlate.pose.position.x = response.Xdst[0]
        posePlate.pose.position.y = response.Ydst[0]
        #rospy.logwarn("SP camera(%s, %s)->plate(%s, %s)" % (poseCamera.pose.position.x, 
        #                                                    poseCamera.pose.position.y, 
        #                                                    posePlate.pose.position.x, 
        #                                                    posePlate.pose.position.y))
        
        return posePlate
    
    def Main(self):
        msgPattern = MsgPattern()

        # Publish a goto(0,0) pattern message, and wait for the end effector to initialize.
        msgPattern.mode = 'byshape'
        msgPattern.shape = 'constant'
        msgPattern.points = []
        msgPattern.frame = 'Stage'
        msgPattern.hzPattern = 1.0
        msgPattern.hzPoint = rospy.get_param('actuator/hzPoint', 100.0)
        msgPattern.count = 1
        msgPattern.radius = 0.0
        msgPattern.preempt = True
        self.pubPatternGen.publish (msgPattern)
        while not self.initialized_endeffector:
            rospy.sleep(0.5)
        rospy.sleep(2)
        self.initialized = True

        # Publish the spiral pattern message.
        msgPattern.mode = 'byshape'
        msgPattern.shape = rospy.get_param('calibration/shape', 'spiral')
        msgPattern.points = []
        msgPattern.frame = 'Stage'
        msgPattern.count = -1
        msgPattern.radius = 0.8 * rospy.get_param('arena/radius_inner', 25.4)
        msgPattern.preempt = True
        if msgPattern.shape=='spiral':
            msgPattern.hzPattern = 0.01
        else:
            msgPattern.hzPattern = 0.1
        self.pubPatternGen.publish (msgPattern)

        try:
            rospy.spin()
        except KeyboardInterrupt:
            print "Shutting down"
            # Publish a goto(0,0) pattern message.
            msgPattern.mode = 'byshape'
            msgPattern.shape = 'constant'
            msgPattern.points = []
            msgPattern.frame = 'Stage'
            msgPattern.hz = 1.0
            msgPattern.count = 1
            msgPattern.radius = 0.0
            msgPattern.preempt = True
            self.pubPatternGen.publish (msgPattern)
    
    

if __name__ == '__main__':
    cal = CalibrateStagePlate()
    cal.Main()
    cv.DestroyAllWindows()

