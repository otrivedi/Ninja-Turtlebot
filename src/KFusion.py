import rospy
import numpy as np
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray

def predict(message):
    xp=A*xt
    Pp=np.dot(A,P*np.transpose(A))+q
    H=np.asmatrix([1,1,1])
    
    a=np.dot(H,(Pn*np.transpose(H))+R)
    K=Pn*np.transpose(H)/a
    
    return update(message.data,xp,Pp,K)
    
def update(zt,x_predicted,Pn,K):
    x_posterior=x_predicted+K*(np.transpose(C)*zt-H*x_predicted)
    P_posterior=(np.identity(3)-K*H)*Pn
    xpo,dxpo=x_posterior,P_posterior
    return x_posterior,P_posterior

if __name__ == '__main__':
    try:        
        global A
        global B
        global C
        global R
        global q
        global H
        global xpo
        global dxpo
        global Pt
        strl = "KFiltering node started "
        xpo=0
        dxpo=0
        Pt=0
        R=[[R1,0],[0,R2]]
        C=[[C1],[C2]]
        
        rospy.loginfo(strl)

        rospy.init_node('KFusion')

        subx = rospy.Subscriber("SensorCombinedVals", Float64MultiArray, predict)

        pub = rospy.Publisher('turtle_states', Float64MultiArray, queue_size=10)
        
        rospy.spin()

    except rospy.ROSInterruptException:
        pass