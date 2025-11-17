#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray, Float32


received_result = None
pub = None

def result_callback(msg):
    global received_result
    rospy.loginfo(f"Received result: {msg.data}")
    received_result = msg.data

def send_request(numbers):
    global pub, received_result

    rospy.sleep(1)

    received_result = None

    msg = Float32MultiArray()
    msg.data = numbers
    pub.publish(msg)

    timeout = rospy.Time.now() + rospy.Duration(10)
    while not rospy.is_shutdown() and rospy.Time.now() < timeout:
        if received_result is not None:
            rospy.loginfo(f"Final result: {received_result}")
            return received_result
        rospy.sleep(0.1)

def main():
    global pub
    
    rospy.init_node('request_node')
    
    output_topic = rospy.get_param('~output_topic', 'polynomial_input')
    input_topic = rospy.get_param('~input_topic', 'sum_result')

    pub = rospy.Publisher(output_topic, Float32MultiArray, queue_size=10)
    rospy.Subscriber(input_topic, Float32, result_callback)
    
    numbers = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
    
    try:
        result = send_request(numbers)
        
        if result is not None:
            print(f"Result: {result}")
        else:
            print("Failed to get result")
            sys.exit(1)
            
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()