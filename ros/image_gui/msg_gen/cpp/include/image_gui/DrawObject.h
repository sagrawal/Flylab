/* Auto-generated by genmsg_cpp for file /home/ssafarik/git/Flyatar2/ros/image_gui/msg/DrawObject.msg */
#ifndef IMAGE_GUI_MESSAGE_DRAWOBJECT_H
#define IMAGE_GUI_MESSAGE_DRAWOBJECT_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "image_gui/CvPoint.h"
#include "image_gui/CvLine.h"
#include "image_gui/CvCircle.h"

namespace image_gui
{
template <class ContainerAllocator>
struct DrawObject_ {
  typedef DrawObject_<ContainerAllocator> Type;

  DrawObject_()
  : show(false)
  , object_center()
  , line_list()
  , circle_list()
  {
  }

  DrawObject_(const ContainerAllocator& _alloc)
  : show(false)
  , object_center(_alloc)
  , line_list(_alloc)
  , circle_list(_alloc)
  {
  }

  typedef uint8_t _show_type;
  uint8_t show;

  typedef  ::image_gui::CvPoint_<ContainerAllocator>  _object_center_type;
   ::image_gui::CvPoint_<ContainerAllocator>  object_center;

  typedef std::vector< ::image_gui::CvLine_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvLine_<ContainerAllocator> >::other >  _line_list_type;
  std::vector< ::image_gui::CvLine_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvLine_<ContainerAllocator> >::other >  line_list;

  typedef std::vector< ::image_gui::CvCircle_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvCircle_<ContainerAllocator> >::other >  _circle_list_type;
  std::vector< ::image_gui::CvCircle_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvCircle_<ContainerAllocator> >::other >  circle_list;


  ROS_DEPRECATED uint32_t get_line_list_size() const { return (uint32_t)line_list.size(); }
  ROS_DEPRECATED void set_line_list_size(uint32_t size) { line_list.resize((size_t)size); }
  ROS_DEPRECATED void get_line_list_vec(std::vector< ::image_gui::CvLine_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvLine_<ContainerAllocator> >::other > & vec) const { vec = this->line_list; }
  ROS_DEPRECATED void set_line_list_vec(const std::vector< ::image_gui::CvLine_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvLine_<ContainerAllocator> >::other > & vec) { this->line_list = vec; }
  ROS_DEPRECATED uint32_t get_circle_list_size() const { return (uint32_t)circle_list.size(); }
  ROS_DEPRECATED void set_circle_list_size(uint32_t size) { circle_list.resize((size_t)size); }
  ROS_DEPRECATED void get_circle_list_vec(std::vector< ::image_gui::CvCircle_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvCircle_<ContainerAllocator> >::other > & vec) const { vec = this->circle_list; }
  ROS_DEPRECATED void set_circle_list_vec(const std::vector< ::image_gui::CvCircle_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::image_gui::CvCircle_<ContainerAllocator> >::other > & vec) { this->circle_list = vec; }
private:
  static const char* __s_getDataType_() { return "image_gui/DrawObject"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "2384beb9729e341fbbc183cc2845fddf"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "bool show\n\
CvPoint object_center\n\
CvLine[] line_list\n\
CvCircle[] circle_list\n\
================================================================================\n\
MSG: image_gui/CvPoint\n\
int32 x\n\
int32 y\n\
\n\
================================================================================\n\
MSG: image_gui/CvLine\n\
CvPoint point1\n\
CvPoint point2\n\
CvColor color\n\
int32 thickness\n\
int32 lineType\n\
int32 shift\n\
================================================================================\n\
MSG: image_gui/CvColor\n\
float64 red\n\
float64 green\n\
float64 blue\n\
================================================================================\n\
MSG: image_gui/CvCircle\n\
CvPoint center\n\
int32 radius\n\
CvColor color\n\
int32 thickness\n\
int32 lineType\n\
int32 shift\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, show);
    ros::serialization::serialize(stream, object_center);
    ros::serialization::serialize(stream, line_list);
    ros::serialization::serialize(stream, circle_list);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, show);
    ros::serialization::deserialize(stream, object_center);
    ros::serialization::deserialize(stream, line_list);
    ros::serialization::deserialize(stream, circle_list);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(show);
    size += ros::serialization::serializationLength(object_center);
    size += ros::serialization::serializationLength(line_list);
    size += ros::serialization::serializationLength(circle_list);
    return size;
  }

  typedef boost::shared_ptr< ::image_gui::DrawObject_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::image_gui::DrawObject_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DrawObject
typedef  ::image_gui::DrawObject_<std::allocator<void> > DrawObject;

typedef boost::shared_ptr< ::image_gui::DrawObject> DrawObjectPtr;
typedef boost::shared_ptr< ::image_gui::DrawObject const> DrawObjectConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::image_gui::DrawObject_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::image_gui::DrawObject_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace image_gui

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::image_gui::DrawObject_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::image_gui::DrawObject_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::image_gui::DrawObject_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2384beb9729e341fbbc183cc2845fddf";
  }

  static const char* value(const  ::image_gui::DrawObject_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2384beb9729e341fULL;
  static const uint64_t static_value2 = 0xbbc183cc2845fddfULL;
};

template<class ContainerAllocator>
struct DataType< ::image_gui::DrawObject_<ContainerAllocator> > {
  static const char* value() 
  {
    return "image_gui/DrawObject";
  }

  static const char* value(const  ::image_gui::DrawObject_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::image_gui::DrawObject_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool show\n\
CvPoint object_center\n\
CvLine[] line_list\n\
CvCircle[] circle_list\n\
================================================================================\n\
MSG: image_gui/CvPoint\n\
int32 x\n\
int32 y\n\
\n\
================================================================================\n\
MSG: image_gui/CvLine\n\
CvPoint point1\n\
CvPoint point2\n\
CvColor color\n\
int32 thickness\n\
int32 lineType\n\
int32 shift\n\
================================================================================\n\
MSG: image_gui/CvColor\n\
float64 red\n\
float64 green\n\
float64 blue\n\
================================================================================\n\
MSG: image_gui/CvCircle\n\
CvPoint center\n\
int32 radius\n\
CvColor color\n\
int32 thickness\n\
int32 lineType\n\
int32 shift\n\
";
  }

  static const char* value(const  ::image_gui::DrawObject_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::image_gui::DrawObject_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.show);
    stream.next(m.object_center);
    stream.next(m.line_list);
    stream.next(m.circle_list);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DrawObject_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::image_gui::DrawObject_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::image_gui::DrawObject_<ContainerAllocator> & v) 
  {
    s << indent << "show: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.show);
    s << indent << "object_center: ";
s << std::endl;
    Printer< ::image_gui::CvPoint_<ContainerAllocator> >::stream(s, indent + "  ", v.object_center);
    s << indent << "line_list[]" << std::endl;
    for (size_t i = 0; i < v.line_list.size(); ++i)
    {
      s << indent << "  line_list[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::image_gui::CvLine_<ContainerAllocator> >::stream(s, indent + "    ", v.line_list[i]);
    }
    s << indent << "circle_list[]" << std::endl;
    for (size_t i = 0; i < v.circle_list.size(); ++i)
    {
      s << indent << "  circle_list[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::image_gui::CvCircle_<ContainerAllocator> >::stream(s, indent + "    ", v.circle_list[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // IMAGE_GUI_MESSAGE_DRAWOBJECT_H

