#! /usr/bin/env python

import rospy
import actionlib
from my_sphero_actions.msg import getOdomDataAction, getOdomDataResult, getOdomDataGoal


'''
actionlib_msgs/msg/GoalStatus.msg
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
'''
                            
def callback(msg):
  rospy.loginfo(msg)
  global result
  result = msg
  
rospy.init_node("spheroDistActionClient")
client = actionlib.SimpleActionClient('/spheroDistActionServer', getOdomDataAction)
client.wait_for_server()
goal = getOdomDataGoal()
rate = rospy.Rate(0.5)

#while not rospy.is_shutdown():
client.send_goal(goal)
#client.wait_for_result()
while not rospy.is_shutdown():
  result = client.get_result()
  status = client.get_state()
  rospy.loginfo("Status: {}".format(status))
  rospy.loginfo("Result: {}".format(result))
  rate.sleep()
