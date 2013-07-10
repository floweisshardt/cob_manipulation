#! /usr/bin/env python

import roslib; roslib.load_manifest('cob_grasp_generation')
import rospy

import actionlib
import manipulation_msgs.msg
import cob_grasp_generation.msg 

class CobGraspGenerationActionServer(object):
  # create messages that are used to publish feedback/result
  _feedback = cob_grasp_generation.msg.GenerateGraspsFeedback()
  _result   = cob_grasp_generation.msg.GenerateGraspsResult()

  def __init__(self, name):
    self._action_name = name
    self._as = actionlib.SimpleActionServer(self._action_name, cob_grasp_generation.msg.GenerateGraspsAction, execute_cb=self.execute_cb)
    self._as.start()
    
  def execute_cb(self, goal):
    # helper variables
    r = rospy.Rate(1)
    success = False
    grasp_list = []
    
    # publish info to the console for the user
    rospy.loginfo('%s: Executing, generating grasps for %s' % (self._action_name, goal.object_name))
    
    
    
    
    # Do Witalij's fancy grasp_generation
    rospy.sleep(5.0)
    
    
    
    #Fill result
    self._result.success = success
    self._result.grasp_list = grasp_list
    #Set action state
    if success:
      rospy.loginfo('%s: Succeeded' % self._action_name)
      self._as.set_succeeded(self._result)
    else:
      rospy.logwarn('%s: Failed' % self._action_name)
      self._as.set_aborted(self._result)
      
if __name__ == '__main__':
  rospy.init_node('generate_grasps')
  CobGraspGenerationActionServer(rospy.get_name())
  rospy.spin()