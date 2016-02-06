#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import tf
import csv
from datetime import datetime




def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    # define a timestamp format you like
    FORMAT = '%Y_%m_%d_%H:%M:%S'
    path2 = '.csv'
    path1 = '/home/artlabpc3/SkeletonData/data_'
    new_path = '%s%s_%s' % (path1,datetime.now().strftime(FORMAT), path2)
    rospy.init_node('rgbdsensor_listener', anonymous=True)
    l = tf.TransformListener()
    with open(new_path,'w') as f1:
    	w=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    
    	while not rospy.is_shutdown():
        	try:
            		l.waitForTransform('/openni_depth_frame', '/left_hand_1', rospy.Time(), rospy.Duration(4.0))
            		trans, rot = l.lookupTransform('/openni_depth_frame', '/left_hand_1',rospy.Duration())
	    		w.writerow([trans[0], trans[1], trans[2]])
            
        	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                	continue
    
    
    
    



    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    
    listener()

