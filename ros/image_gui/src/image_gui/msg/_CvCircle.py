"""autogenerated by genmsg_py from CvCircle.msg. Do not edit."""
import roslib.message
import struct

import image_gui.msg

class CvCircle(roslib.message.Message):
  _md5sum = "a60e9679b4eefa3cfeca04ca12c0783c"
  _type = "image_gui/CvCircle"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """CvPoint center
int32 radius
CvColor color
int32 thickness
int32 lineType
int32 shift
================================================================================
MSG: image_gui/CvPoint
int32 x
int32 y

================================================================================
MSG: image_gui/CvColor
float64 red
float64 green
float64 blue
"""
  __slots__ = ['center','radius','color','thickness','lineType','shift']
  _slot_types = ['image_gui/CvPoint','int32','image_gui/CvColor','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       center,radius,color,thickness,lineType,shift
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(CvCircle, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.center is None:
        self.center = image_gui.msg.CvPoint()
      if self.radius is None:
        self.radius = 0
      if self.color is None:
        self.color = image_gui.msg.CvColor()
      if self.thickness is None:
        self.thickness = 0
      if self.lineType is None:
        self.lineType = 0
      if self.shift is None:
        self.shift = 0
    else:
      self.center = image_gui.msg.CvPoint()
      self.radius = 0
      self.color = image_gui.msg.CvColor()
      self.thickness = 0
      self.lineType = 0
      self.shift = 0

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
      buff.write(_struct_3i3d3i.pack(_x.center.x, _x.center.y, _x.radius, _x.color.red, _x.color.green, _x.color.blue, _x.thickness, _x.lineType, _x.shift))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.center is None:
        self.center = image_gui.msg.CvPoint()
      if self.color is None:
        self.color = image_gui.msg.CvColor()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.center.x, _x.center.y, _x.radius, _x.color.red, _x.color.green, _x.color.blue, _x.thickness, _x.lineType, _x.shift,) = _struct_3i3d3i.unpack(str[start:end])
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
      buff.write(_struct_3i3d3i.pack(_x.center.x, _x.center.y, _x.radius, _x.color.red, _x.color.green, _x.color.blue, _x.thickness, _x.lineType, _x.shift))
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
      if self.center is None:
        self.center = image_gui.msg.CvPoint()
      if self.color is None:
        self.color = image_gui.msg.CvColor()
      end = 0
      _x = self
      start = end
      end += 48
      (_x.center.x, _x.center.y, _x.radius, _x.color.red, _x.color.green, _x.color.blue, _x.thickness, _x.lineType, _x.shift,) = _struct_3i3d3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3i3d3i = struct.Struct("<3i3d3i")