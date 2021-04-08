#!/usr/bin/env python3
#an algorith to calculate an approximate value of "e" using the Euler methode 
#to solve ODE (y'-y=0 for y(0)=1 
def Euler(n=10000000): 
	h = 1 / n; 
	y = [1];
	y.append(1);
	for i in range(0, n+1, 1):
	
		y.insert(i+1, y[i]*(1+h));
	return {'e':y[n],'error':h/2} ;
print(Euler());
