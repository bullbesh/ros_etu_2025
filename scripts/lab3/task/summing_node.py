#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray, Float32


pub = None

def callback(msg):
    global pub

    total_sum = sum(msg.data)
    
    rospy.loginfo(f"Sum result: {total_sum}")

    output_msg = Float32()
    output_msg.data = total_sum
    pub.publish(output_msg)

def main():
    global pub
    
    rospy.init_node('summing_node')

    input_topic = rospy.get_param('~input_topic', 'summing_input')
    output_topic = rospy.get_param('~output_topic', 'sum_result')

    pub = rospy.Publisher(output_topic, Float32, queue_size=10)
    rospy.Subscriber(input_topic, Float32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass