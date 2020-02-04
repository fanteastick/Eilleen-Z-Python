# importing
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# this script handles linear regressions and makes two basic plots

def readFile(file):
	df = pd.read_csv(file, sep='\t')
	return df

def printDF(datfra):
	print("getting the info:")
	print(".head")
	print(datfra.head())
	print(".info")
	print (datfra.info())
	print(".tail")
	print(datfra.tail())

def linReg(X_train, y_train, X_test, y_test): 
	regr = linear_model.LinearRegression()
	regr.fit(X_train, y_train)
	y_pred = regr.predict(X_test)
	print('Coefficients: \n', regr.coef_)
	print("Mean squared error: %.2f"
		% mean_squared_error(y_test, y_pred))
	return (y_pred)

def barplot(x_val, y_val, xaxis, yaxis, title):
	plt.bar(x_val, y_val, align='center', alpha=0.5, width = .02)
	#how do I do xticks and yticks
	plt.ylabel(xaxis)
	plt.xlabel(yaxis)
	plt.title(title)
	plt.show()

def scatterplot(x_val, y_val, xaxis, yaxis, title):
	plt.scatter(x_val, y_val)
	plt.xlabel(xaxis)
	plt.ylabel(yaxis)
	plt.title(title)

	plt.xlim(xmax =6) #setting the same axes scaling for both sides
	plt.ylim(ymax=6)
	
	plt.show()


df = readFile('pmc_breakdown_gen.csv')
df_target = df['Actual Power_A15']
df.rename(columns={"Unnamed: 0": "Workload Number"}, inplace=True)
printDF(df)
df_train = df.drop(['Core Mask', 'Workload Name', 'Actual Power_A15', 'Signed Errors', 'Relative pc Errors', 'Squared Errors', 'Predicted Power_A15'], axis=1)

X_train, X_test, y_train, y_test= train_test_split(df_train, df_target, test_size=0.25, random_state=42)
y_pred = linReg(X_train, y_train, X_test, y_test)
barplot(y_pred, y_test, 'y_pred', 'y_test', 'the graph')
scatterplot(y_pred, y_test, 'y_pred', 'y_test', 'second graph')