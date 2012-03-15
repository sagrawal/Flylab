"""autogenerated by genmsg_py from ActionStageStateAction.msg. Do not edit."""
import roslib.message
import struct

import stage_action_server.msg
import roslib.rostime
import actionlib_msgs.msg
import flycore.msg
import geometry_msgs.msg
import std_msgs.msg

class ActionStageStateAction(roslib.message.Message):
  _md5sum = "4f09ddf3684b9b5d44d009bf5e42fd76"
  _type = "stage_action_server/ActionStageStateAction"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

ActionStageStateActionGoal action_goal
ActionStageStateActionResult action_result
ActionStageStateActionFeedback action_feedback

================================================================================
MSG: stage_action_server/ActionStageStateActionGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
ActionStageStateGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: stage_action_server/ActionStageStateGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
flycore/MsgFrameState state

================================================================================
MSG: flycore/MsgFrameState
Header header
geometry_msgs/Pose pose
geometry_msgs/Twist velocity


================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into it's linear and angular parts. 
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: stage_action_server/ActionStageStateActionResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
ActionStageStateResult result

================================================================================
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


================================================================================
MSG: stage_action_server/ActionStageStateResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
flycore/MsgFrameState state

================================================================================
MSG: stage_action_server/ActionStageStateActionFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
ActionStageStateFeedback feedback

================================================================================
MSG: stage_action_server/ActionStageStateFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
flycore/MsgFrameState state


"""
  __slots__ = ['action_goal','action_result','action_feedback']
  _slot_types = ['stage_action_server/ActionStageStateActionGoal','stage_action_server/ActionStageStateActionResult','stage_action_server/ActionStageStateActionFeedback']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       action_goal,action_result,action_feedback
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(ActionStageStateAction, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.action_goal is None:
        self.action_goal = stage_action_server.msg.ActionStageStateActionGoal()
      if self.action_result is None:
        self.action_result = stage_action_server.msg.ActionStageStateActionResult()
      if self.action_feedback is None:
        self.action_feedback = stage_action_server.msg.ActionStageStateActionFeedback()
    else:
      self.action_goal = stage_action_server.msg.ActionStageStateActionGoal()
      self.action_result = stage_action_server.msg.ActionStageStateActionResult()
      self.action_feedback = stage_action_server.msg.ActionStageStateActionFeedback()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs))
      _x = self.action_goal.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs))
      _x = self.action_goal.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.action_goal.goal.state.header.seq, _x.action_goal.goal.state.header.stamp.secs, _x.action_goal.goal.state.header.stamp.nsecs))
      _x = self.action_goal.goal.state.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d3I.pack(_x.action_goal.goal.state.pose.position.x, _x.action_goal.goal.state.pose.position.y, _x.action_goal.goal.state.pose.position.z, _x.action_goal.goal.state.pose.orientation.x, _x.action_goal.goal.state.pose.orientation.y, _x.action_goal.goal.state.pose.orientation.z, _x.action_goal.goal.state.pose.orientation.w, _x.action_goal.goal.state.velocity.linear.x, _x.action_goal.goal.state.velocity.linear.y, _x.action_goal.goal.state.velocity.linear.z, _x.action_goal.goal.state.velocity.angular.x, _x.action_goal.goal.state.velocity.angular.y, _x.action_goal.goal.state.velocity.angular.z, _x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs))
      _x = self.action_result.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs))
      _x = self.action_result.status.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.action_result.status.status))
      _x = self.action_result.status.text
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.action_result.result.state.header.seq, _x.action_result.result.state.header.stamp.secs, _x.action_result.result.state.header.stamp.nsecs))
      _x = self.action_result.result.state.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d3I.pack(_x.action_result.result.state.pose.position.x, _x.action_result.result.state.pose.position.y, _x.action_result.result.state.pose.position.z, _x.action_result.result.state.pose.orientation.x, _x.action_result.result.state.pose.orientation.y, _x.action_result.result.state.pose.orientation.z, _x.action_result.result.state.pose.orientation.w, _x.action_result.result.state.velocity.linear.x, _x.action_result.result.state.velocity.linear.y, _x.action_result.result.state.velocity.linear.z, _x.action_result.result.state.velocity.angular.x, _x.action_result.result.state.velocity.angular.y, _x.action_result.result.state.velocity.angular.z, _x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs))
      _x = self.action_feedback.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs))
      _x = self.action_feedback.status.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.action_feedback.status.status))
      _x = self.action_feedback.status.text
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.action_feedback.feedback.state.header.seq, _x.action_feedback.feedback.state.header.stamp.secs, _x.action_feedback.feedback.state.header.stamp.nsecs))
      _x = self.action_feedback.feedback.state.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d.pack(_x.action_feedback.feedback.state.pose.position.x, _x.action_feedback.feedback.state.pose.position.y, _x.action_feedback.feedback.state.pose.position.z, _x.action_feedback.feedback.state.pose.orientation.x, _x.action_feedback.feedback.state.pose.orientation.y, _x.action_feedback.feedback.state.pose.orientation.z, _x.action_feedback.feedback.state.pose.orientation.w, _x.action_feedback.feedback.state.velocity.linear.x, _x.action_feedback.feedback.state.velocity.linear.y, _x.action_feedback.feedback.state.velocity.linear.z, _x.action_feedback.feedback.state.velocity.angular.x, _x.action_feedback.feedback.state.velocity.angular.y, _x.action_feedback.feedback.state.velocity.angular.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.action_goal is None:
        self.action_goal = stage_action_server.msg.ActionStageStateActionGoal()
      if self.action_result is None:
        self.action_result = stage_action_server.msg.ActionStageStateActionResult()
      if self.action_feedback is None:
        self.action_feedback = stage_action_server.msg.ActionStageStateActionFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_goal.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_goal.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.action_goal.goal.state.header.seq, _x.action_goal.goal.state.header.stamp.secs, _x.action_goal.goal.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_goal.goal.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 116
      (_x.action_goal.goal.state.pose.position.x, _x.action_goal.goal.state.pose.position.y, _x.action_goal.goal.state.pose.position.z, _x.action_goal.goal.state.pose.orientation.x, _x.action_goal.goal.state.pose.orientation.y, _x.action_goal.goal.state.pose.orientation.z, _x.action_goal.goal.state.pose.orientation.w, _x.action_goal.goal.state.velocity.linear.x, _x.action_goal.goal.state.velocity.linear.y, _x.action_goal.goal.state.velocity.linear.z, _x.action_goal.goal.state.velocity.angular.x, _x.action_goal.goal.state.velocity.angular.y, _x.action_goal.goal.state.velocity.angular.z, _x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs,) = _struct_13d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_result.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.action_result.result.state.header.seq, _x.action_result.result.state.header.stamp.secs, _x.action_result.result.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.result.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 116
      (_x.action_result.result.state.pose.position.x, _x.action_result.result.state.pose.position.y, _x.action_result.result.state.pose.position.z, _x.action_result.result.state.pose.orientation.x, _x.action_result.result.state.pose.orientation.y, _x.action_result.result.state.pose.orientation.z, _x.action_result.result.state.pose.orientation.w, _x.action_result.result.state.velocity.linear.x, _x.action_result.result.state.velocity.linear.y, _x.action_result.result.state.velocity.linear.z, _x.action_result.result.state.velocity.angular.x, _x.action_result.result.state.velocity.angular.y, _x.action_result.result.state.velocity.angular.z, _x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs,) = _struct_13d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_feedback.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.action_feedback.feedback.state.header.seq, _x.action_feedback.feedback.state.header.stamp.secs, _x.action_feedback.feedback.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.feedback.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 104
      (_x.action_feedback.feedback.state.pose.position.x, _x.action_feedback.feedback.state.pose.position.y, _x.action_feedback.feedback.state.pose.position.z, _x.action_feedback.feedback.state.pose.orientation.x, _x.action_feedback.feedback.state.pose.orientation.y, _x.action_feedback.feedback.state.pose.orientation.z, _x.action_feedback.feedback.state.pose.orientation.w, _x.action_feedback.feedback.state.velocity.linear.x, _x.action_feedback.feedback.state.velocity.linear.y, _x.action_feedback.feedback.state.velocity.linear.z, _x.action_feedback.feedback.state.velocity.angular.x, _x.action_feedback.feedback.state.velocity.angular.y, _x.action_feedback.feedback.state.velocity.angular.z,) = _struct_13d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs))
      _x = self.action_goal.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs))
      _x = self.action_goal.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.action_goal.goal.state.header.seq, _x.action_goal.goal.state.header.stamp.secs, _x.action_goal.goal.state.header.stamp.nsecs))
      _x = self.action_goal.goal.state.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d3I.pack(_x.action_goal.goal.state.pose.position.x, _x.action_goal.goal.state.pose.position.y, _x.action_goal.goal.state.pose.position.z, _x.action_goal.goal.state.pose.orientation.x, _x.action_goal.goal.state.pose.orientation.y, _x.action_goal.goal.state.pose.orientation.z, _x.action_goal.goal.state.pose.orientation.w, _x.action_goal.goal.state.velocity.linear.x, _x.action_goal.goal.state.velocity.linear.y, _x.action_goal.goal.state.velocity.linear.z, _x.action_goal.goal.state.velocity.angular.x, _x.action_goal.goal.state.velocity.angular.y, _x.action_goal.goal.state.velocity.angular.z, _x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs))
      _x = self.action_result.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs))
      _x = self.action_result.status.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.action_result.status.status))
      _x = self.action_result.status.text
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.action_result.result.state.header.seq, _x.action_result.result.state.header.stamp.secs, _x.action_result.result.state.header.stamp.nsecs))
      _x = self.action_result.result.state.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d3I.pack(_x.action_result.result.state.pose.position.x, _x.action_result.result.state.pose.position.y, _x.action_result.result.state.pose.position.z, _x.action_result.result.state.pose.orientation.x, _x.action_result.result.state.pose.orientation.y, _x.action_result.result.state.pose.orientation.z, _x.action_result.result.state.pose.orientation.w, _x.action_result.result.state.velocity.linear.x, _x.action_result.result.state.velocity.linear.y, _x.action_result.result.state.velocity.linear.z, _x.action_result.result.state.velocity.angular.x, _x.action_result.result.state.velocity.angular.y, _x.action_result.result.state.velocity.angular.z, _x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs))
      _x = self.action_feedback.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs))
      _x = self.action_feedback.status.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.action_feedback.status.status))
      _x = self.action_feedback.status.text
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.action_feedback.feedback.state.header.seq, _x.action_feedback.feedback.state.header.stamp.secs, _x.action_feedback.feedback.state.header.stamp.nsecs))
      _x = self.action_feedback.feedback.state.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d.pack(_x.action_feedback.feedback.state.pose.position.x, _x.action_feedback.feedback.state.pose.position.y, _x.action_feedback.feedback.state.pose.position.z, _x.action_feedback.feedback.state.pose.orientation.x, _x.action_feedback.feedback.state.pose.orientation.y, _x.action_feedback.feedback.state.pose.orientation.z, _x.action_feedback.feedback.state.pose.orientation.w, _x.action_feedback.feedback.state.velocity.linear.x, _x.action_feedback.feedback.state.velocity.linear.y, _x.action_feedback.feedback.state.velocity.linear.z, _x.action_feedback.feedback.state.velocity.angular.x, _x.action_feedback.feedback.state.velocity.angular.y, _x.action_feedback.feedback.state.velocity.angular.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.action_goal is None:
        self.action_goal = stage_action_server.msg.ActionStageStateActionGoal()
      if self.action_result is None:
        self.action_result = stage_action_server.msg.ActionStageStateActionResult()
      if self.action_feedback is None:
        self.action_feedback = stage_action_server.msg.ActionStageStateActionFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_goal.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_goal.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.action_goal.goal.state.header.seq, _x.action_goal.goal.state.header.stamp.secs, _x.action_goal.goal.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_goal.goal.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 116
      (_x.action_goal.goal.state.pose.position.x, _x.action_goal.goal.state.pose.position.y, _x.action_goal.goal.state.pose.position.z, _x.action_goal.goal.state.pose.orientation.x, _x.action_goal.goal.state.pose.orientation.y, _x.action_goal.goal.state.pose.orientation.z, _x.action_goal.goal.state.pose.orientation.w, _x.action_goal.goal.state.velocity.linear.x, _x.action_goal.goal.state.velocity.linear.y, _x.action_goal.goal.state.velocity.linear.z, _x.action_goal.goal.state.velocity.angular.x, _x.action_goal.goal.state.velocity.angular.y, _x.action_goal.goal.state.velocity.angular.z, _x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs,) = _struct_13d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_result.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.action_result.result.state.header.seq, _x.action_result.result.state.header.stamp.secs, _x.action_result.result.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_result.result.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 116
      (_x.action_result.result.state.pose.position.x, _x.action_result.result.state.pose.position.y, _x.action_result.result.state.pose.position.z, _x.action_result.result.state.pose.orientation.x, _x.action_result.result.state.pose.orientation.y, _x.action_result.result.state.pose.orientation.z, _x.action_result.result.state.pose.orientation.w, _x.action_result.result.state.velocity.linear.x, _x.action_result.result.state.velocity.linear.y, _x.action_result.result.state.velocity.linear.z, _x.action_result.result.state.velocity.angular.x, _x.action_result.result.state.velocity.angular.y, _x.action_result.result.state.velocity.angular.z, _x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs,) = _struct_13d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_feedback.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.action_feedback.feedback.state.header.seq, _x.action_feedback.feedback.state.header.stamp.secs, _x.action_feedback.feedback.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.action_feedback.feedback.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 104
      (_x.action_feedback.feedback.state.pose.position.x, _x.action_feedback.feedback.state.pose.position.y, _x.action_feedback.feedback.state.pose.position.z, _x.action_feedback.feedback.state.pose.orientation.x, _x.action_feedback.feedback.state.pose.orientation.y, _x.action_feedback.feedback.state.pose.orientation.z, _x.action_feedback.feedback.state.pose.orientation.w, _x.action_feedback.feedback.state.velocity.linear.x, _x.action_feedback.feedback.state.velocity.linear.y, _x.action_feedback.feedback.state.velocity.linear.z, _x.action_feedback.feedback.state.velocity.angular.x, _x.action_feedback.feedback.state.velocity.angular.y, _x.action_feedback.feedback.state.velocity.angular.z,) = _struct_13d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_13d3I = struct.Struct("<13d3I")
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_2I = struct.Struct("<2I")
_struct_13d = struct.Struct("<13d")
