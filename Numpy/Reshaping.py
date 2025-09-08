import numpy as np

a=np.arange(12) #0 to 11 1*1 matrix  
print("Before Reshape : ",a)
reshaped=a.reshape(3,4) #Same values, but 3*4 matrix this time

print("After reshaping : ",reshaped)