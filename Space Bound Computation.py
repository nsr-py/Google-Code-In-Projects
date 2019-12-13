import numpy as np 
import matplotlib.pyplot as plt 
import time

# I will be flattening the array using np.ravel
def compute(arr):	
	#row major
	tr = time.time()
	test = np.ravel(arr)
	tr = time.time() - tr
	#column major
	tc = time.time()
	test = np.ravel(arr, order='F')
	tc = time.time() - tc

	return (tr,tc)

#trm : Time-row-major
#tcm : Time-column-major
def plot(num,trm,tcm):
	plt.plot(num,trm,color='blue',label='Row-Major')
	plt.plot(num,tcm,color='red',label='Column-Major')
	plt.xlabel("Size of array")
	plt.ylabel("Time")
	plt.title("Time vs Size of Array")
	plt.legend()

trm = []
tcm = []
num = []

no_of_experiments = int(input("How many tests do you want to run?   "))
print("\n 	Enter sizes of test square array into the  list : \n")
for _ in range(no_of_experiments):
	num.append(int(input()))
for i in range(no_of_experiments):
	n = num[i]
	a = np.random.randint(10,size=(n,n))
	tr , tc = compute(a)
	trm.append(tr)
	tcm.append(tc)
	

plot(num,trm,tcm)