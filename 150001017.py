import numpy as np
a = [1,1,1,1] 										# Vector 1 for storing pattern 1
a = np.asmatrix(a)
b = [1,1,-1,-1] 									# Vector 2 for storing pattern 2
b = np.asmatrix(b)
I = np.eye(4) 										# Identity matrix of 4x4 
wt = np.dot(a.T,a) - 2*I + np.dot(b.T,b)						# Calculating weight matrix 
ip = [[1,1,1,1],[1,1,-1,-1],[1,1,1,0]]							# Creating array for storing given inputs 
update = [1,4,3,2]									# Vector for storing asynchronous update rule 
theta = 1 										# Used in updating y according to the output given by net 
update = np.asarray(update)
temp = np.copy(ip)
temp = np.asmatrix(temp)

for ind in range(0,temp.shape[0]) :
	print("starting for input : {}".format(ind+1))
	print("input : {}".format(temp[ind]))
	cnt = 0
	y = np.copy(temp[ind])
	y = np.asmatrix(y)								# Creating a vector for storing previous results for convergence test 
	resprev = np.copy(y)
	resprev = np.asmatrix(resprev)
	for i in range(0,y.shape[1]) :
		net = temp[ind][0,update[i]-1] + np.dot(y,(wt[update[i]-1]).T) - y[0,update[i]-1]*wt[update[i]-1,update[i]-1] 		# Calculating NET 
		print("net : {}".format(net))
		if net[0,0] > theta :							# Conditions for updating corresponding y value 
			y[0,update[i]-1] = 1
		elif net[0,0] == theta :
			y[0,update[i]-1] = y[0,update[i]-1]
		elif net[0,0] < theta :
			y[0,update[i]-1] = 0
			

	cnt += 1 
	print("y after iteration {} : {}".format(cnt,y))
	print("previous result : {}".format(resprev))
	if not (y == resprev).all() :
		while True :
			if (y == resprev).all() :
				break 
			resprev = np.copy(y)
			resprev = np.asmatrix(resprev)
			for i in range(0,y.shape[1]) :
				net = temp[ind][0,update[i]-1] + np.dot(y,(wt[update[i]-1]).T) - y[0,update[i]-1]*wt[update[i]-1,update[i]-1]
				print("net : {}".format(net))
				if net[0,0] > theta :
						y[0,update[i]-1] = 1
				elif net[0,0] == theta :
						y[0,update[i]-1] = y[0,update[i]-1]
				elif net[0,0] < theta :
						y[0,update[i]-1] = 0
				
				
			cnt += 1 
			print("y after iteration {} : {}".format(cnt,y))
			print("previous result : {}".format(resprev))

	print("y final : {}".format(y))   						# Converged value for y. It is the best possible value for the given asynchronous update rule. 
