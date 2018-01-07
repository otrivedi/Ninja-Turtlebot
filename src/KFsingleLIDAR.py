import rospy
import numpy as np
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray

def predict(message):
    B=np.array([[0.1*math.cos(xpo[2])/2,0.1*math.cos(xpo[2])/2],[0.1*math.sin(xpo[2])/2,0.1*math.sin(xpo[2])/2],[0.05,-0.05]])
    xp=A*xpo+B*dxt
    Pp=np.dot(A,Ppo*np.transpose(A))+q
    #H=np.asmatrix([1,1,1,])

    a=np.dot(H,(Pn*np.transpose(H))+R)
    K=Pn*np.transpose(H)/a

    return update(message.data,xp,Pp,K)

def update(zt,x_predicted,Pn,K):
    x_posterior=x_predicted+K*(np.transpose(C)*zt-H*x_predicted)
    P_posterior=(np.identity(3)-K*H)*Pn
    xpo,Ppo=x_posterior,P_posterior
    return x_posterior,P_posterior

if __name__ == '__main__':
    try:
        time_del=0.1
        A=np.array([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
        C=[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        R
        q
        H=np.asmatrix([1,1,1,0,0,0])

        strl = "KFiltering node started "
        xpo=[0,0,0,0,0,0]
        Ppo=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        B=np.array([[0.1/2,0.1/2],[0,0],[0.05,-0.05]])
        rospy.loginfo(strl)

        rospy.init_node('KF')

        subx = rospy.Subscriber("x", Float64, predict)
        #subdx = rospy.Subscriber("x_dot", Float64, resetCallback)
        pub = rospy.Publisher('turtle_states', Float64MultiArray, queue_size=10)

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
