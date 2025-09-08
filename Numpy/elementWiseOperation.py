import numpy as np
left_wheels=np.array([2,3,4]) #m/s
right_wheels=np.array([2,2.5,3])

avg_speed=(left_wheels+right_wheels)/2
print("Average Speed : ",avg_speed)
