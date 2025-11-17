#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray


pub = None

def callback(msg):
    global pub
    rospy.loginfo(f"Received numbers: {msg.data}")

    processed_numbers = []
    for i, num in enumerate(msg.data):
        # i=0: x^3, i=1: x^2, i=2: x^1
        power = 3 - i
        result = num ** power
        processed_numbers.append(result)
    
    rospy.loginfo(f"Processed numbers (powers): {processed_numbers}")

    output_msg = Float32MultiArray()
    output_msg.data = processed_numbers
    pub.publish(output_msg)

def main():
    global pub
    
    rospy.init_node('polynominal_node')

    input_topic = rospy.get_param('~input_topic', 'polynomial_input')
    output_topic = rospy.get_param('~output_topic', 'summing_input')

    pub = rospy.Publisher(output_topic, Float32MultiArray, queue_size=10)
    rospy.Subscriber(input_topic, Float32MultiArray, callback)
    
    rospy.loginfo("Polynominal node started")
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass