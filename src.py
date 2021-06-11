import requests
import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
sys.stdout=open("output.out","w")
Historical="http://data.fixer.io/api/"
KEY="7f1a676a0f8bdc07c369f62c890679bc"
X=[]
Y=[]
for i in range(2000,2021):
	year=i
	add=str(year)+"-09"+"-27"
	new_url=Historical+add
	print(new_url)
	Parameter={"access_key":KEY,"symbols":"USD"}
	response=requests.get(new_url,params=Parameter)
	response=response.json()
	Y.append(response['rates']['USD'])
	X.append(str(i))
X1=[]
Y1=[]
for i in range(2000,2021):
	year=i
	add=str(year)+"-09"+"-27"
	new_url=Historical+add
	print(new_url)
	Parameter={"access_key":KEY,"symbols":"CAD"}
	response=requests.get(new_url,params=Parameter)
	response=response.json()
	Y1.append(response['rates']['CAD'])
	X1.append(str(i))
plt.title('Euro to CAD conversion')
plt.xlabel("YEARS")
plt.ylabel("Euro in CAD")
plt.plot(X1,Y1)
plt.plot(X,Y)
plt.legend(["EUR TO USD","EUR TO CAD"],loc="lower right")
plt.show()

