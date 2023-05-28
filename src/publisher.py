#!/usr/bin/env python3
import rospy
from std_msgs.msg import String



def talker():
	rospy.init_node("publisher")
	pub=rospy.Publisher("published_topic",String,queue_size=10)
	rate=rospy.Rate(30)
	if rospy.has_param("~message"):
		private_param=rospy.get_param("~message")
	else:
		private_param="Default"
	while not rospy.is_shutdown():
		message=String()
		message.data=private_param
		pub.publish(message)
		rate.sleep()

if __name__=="__main__":
	talker()
