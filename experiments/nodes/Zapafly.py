#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('experiments')
import rospy
import numpy as N
import ExperimentLib
from experiments.srv import *
from galvodirector.msg import MsgGalvoCommand
from patterngen.msg import MsgPattern
from tracking.msg import ArenaState




#######################################################################################################
class ExperimentZapafly():
    def __init__(self):
        rospy.init_node('Experiment')
        
#        # Fill out the data structure that defines the experiment.
#        self.experimentparams = ExperimentParamsRequest()
#        
#        self.experimentparams.experiment.description = "Aim laser at fly"
#        self.experimentparams.experiment.maxTrials = -1
#        self.experimentparams.experiment.trial = 1
#        
#        self.experimentparams.save.filenamebase = "zap"
#        self.experimentparams.save.arenastate = False
#        self.experimentparams.save.video = False
#        self.experimentparams.save.bag = False
#        self.experimentparams.save.onlyWhileTriggered = True
#        
#        self.experimentparams.home.enabled = False
#        self.experimentparams.home.x = 0.0
#        self.experimentparams.home.y = 0.0
#        self.experimentparams.home.speed = 20
#        self.experimentparams.home.timeout = -1
#        self.experimentparams.home.tolerance = 2
#        
#        self.experimentparams.waitEntry = 0.0
#        
#        self.experimentparams.triggerEntry.enabled = False
#        self.experimentparams.triggerEntry.distanceMin =   0.0
#        self.experimentparams.triggerEntry.distanceMax = 999.0
#        self.experimentparams.triggerEntry.speedMin =   0.0
#        self.experimentparams.triggerEntry.speedMax = 999.0
#        self.experimentparams.triggerEntry.angleMin =  0.0 * N.pi / 180.0
#        self.experimentparams.triggerEntry.angleMax =180.0 * N.pi / 180.0
#        self.experimentparams.triggerEntry.angleTest = 'inclusive'
#        self.experimentparams.triggerEntry.angleTestBilateral = True
#        self.experimentparams.triggerEntry.timeHold = 0.0
#        self.experimentparams.triggerEntry.timeout = -1
#        
#        self.experimentparams.move.enabled = True
#        self.experimentparams.move.mode = 'relative'        
#        self.experimentparams.move.relative.tracking = True
#        self.experimentparams.move.relative.frameidOriginPosition = "Fly1"
#        self.experimentparams.move.relative.frameidOriginAngle = "Fly1"
#        self.experimentparams.move.relative.distance = 5
#        self.experimentparams.move.relative.angle = 180.0 * N.pi / 180.0
#        self.experimentparams.move.relative.angleType = 'constant'
#        self.experimentparams.move.relative.speed = 200
#        self.experimentparams.move.relative.speedType = 'constant'
#        self.experimentparams.move.relative.tolerance = -1.0 # i.e. never get there.
#        self.experimentparams.move.timeout = 600
#        
#        self.experimentparams.triggerExit.enabled = False
#        self.experimentparams.triggerExit.distanceMin = 0.0
#        self.experimentparams.triggerExit.distanceMax = 999.0
#        self.experimentparams.triggerExit.speedMin =  0.0
#        self.experimentparams.triggerExit.speedMax = 999.0
#        self.experimentparams.triggerExit.angleMin =  0.0 * N.pi / 180.0
#        self.experimentparams.triggerExit.angleMax =180.0 * N.pi / 180.0
#        self.experimentparams.triggerExit.angleTest = 'inclusive'
#        self.experimentparams.triggerExit.angleTestBilateral = True
#        self.experimentparams.triggerExit.timeHold = 0.0
#        self.experimentparams.triggerExit.timeout = -1
#
#        self.experiment = ExperimentLib.Experiment(self.experimentparams)

        #self.subArenaState = rospy.Subscriber('ArenaState', ArenaState, self.ArenaState_callback, queue_size=2)
        self.pubGalvoCommand = rospy.Publisher('GalvoDirector/command', MsgGalvoCommand)


    def TrackFly1(self):
        pattern = MsgPattern()
        pattern.mode       = 'byshape'
        pattern.shape      = 'grid'
        pattern.frame_id   = 'Fly1'
        pattern.hzPattern  = 40.0
        pattern.hzPoint    = 1000.0
        pattern.count      = 1
        pattern.points     = []
        pattern.radius     = 5
        pattern.preempt    = False
    
        command = MsgGalvoCommand()
        command.frameid_target_list = ['Plate',]
        command.pattern_list = [pattern,]
        command.units = 'millimeters' # 'millimeters' or 'volts'
        self.pubGalvoCommand.publish(command)

        
    def Run(self):
        #self.experiment.Run()
        
        while not rospy.is_shutdown():
            self.TrackFly1() 
            rospy.sleep(10)
        




if __name__ == '__main__':
    experiment = ExperimentZapafly()
    experiment.Run()
        

        
