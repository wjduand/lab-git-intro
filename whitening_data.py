from __future__ import print_function
import torch
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
import numpy as np
#reference: http://ufldl.stanford.edu/tutorial/unsupervised/PCAWhitening/
#reference: https://mccormickml.com/2014/06/03/deep-learning-tutorial-pca-and-whitening/

data = torch.load("./assign0_data.py")
def load_and_plot(data):
	x = data[:, 0]
	y = data[:, 1]

	plt.scatter(x, y)
	plt.show()

#data before whitening is correlated and negatively dependent

def zero_means(data):
	data -= torch.mean(data, 0)
	x = data[:, 0]
	y = data[:, 1]
	plt.scatter(x, y)
	plt.show()
	return data


#data after whitening is decorrelated and independent, and points are in quadrants one, two, three, and four
def decorrelate_data(X):
	sigma = np.cov(X, rowvar=False)
	U,S,V = np.linalg.svd(sigma)
	epsilon = 1e-5
	ZCAWhite = np.dot(np.diag(1.0/np.sqrt(S + epsilon)), U.T)
	xZCAWhite = np.dot(np.dot(data, U), ZCAWhite)

	x = xZCAWhite[:, 0]
	y = xZCAWhite[:, 1]

	plt.scatter(x, y)
	plt.show()

load_and_plot(data)
data = zero_means(data)
decorrelate_data(data)
