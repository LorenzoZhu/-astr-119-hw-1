import numpy as np

#integers

i = 10
print(type(i))	#print out the data type of i

a_i = np.zeros(i,dtype=int) #declare ana array of ints
print(type(a_i))			#will return ndarray
print(type(a_i[0]))			#will return int64

#floats

x = 119.0
print(type(x))	#print out the data type of x

y = 1.19e2
print(type(y))

z = np.zeros(i,dtype=float) #declare array pf floats
print(type(z))				#will return nd array
print(type(z[0]))				#will return float64