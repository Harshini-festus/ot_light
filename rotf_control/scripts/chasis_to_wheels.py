import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
chasis_velocity=rospy.Subscriber("/cmd_vel",Twist,queue_size=1)
left_wheel_velocity=rospy.Publisher("/velocity_controller/left_wheel_controller/command",Float64,queue_size=1)
right_wheel_velocity=rospy.Publisher("/velocity_controller/right_wheel_controller/command",Float64,queue_size=1)
rate=rospy.Rate(10)
vel_l=0
vel_r=0

if __name__=="__main__":
    left_wheel_velocity.publish(vel_l)
    right_wheel_velocity.publish(vel_r)
