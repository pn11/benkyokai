# coding : utf-8

import sys, os
#sys.path append(os.pardir) #　親ディレクトリをPATHに追加
from functions import *
from gradient import numerical_gradient

class TwoLayerNet:
	def __init__(self, input_size, hidden_size, output_size,
				wight_init_std = 0.01): # 入力層、隠れ層、出力層のニューロン数
		# 重みの初期化
		self.params = {}
		# W：重み、b:バイアス
		self.params['W1'] = wight_init_std * np.random.randn(input_size, hidden_size)
		self.params['b1'] = np.zeros(hidden_size)
		self.params['W2'] = wight_init_std * np.random.randn(hidden_size, output_size)
		self.params['b2'] = np.zeros(output_size)
	
	def predict(self, x): #伝播を計算
		W1, W2 = self.params['W1'], self.params['W2']
		b1, b2 = self.params['b1'], self.params['b2']
#		print(x.shape)
#		print(W1.shape)
#		print(b1.shape)
		a1 = np.dot(x, W1) + b1
#		print(a1.shape)
		z1 = sigmoid(a1)
#		print(z1.shape)
		a2 = np.dot(z1, W2) + b2
#		print(a2.shape)
		y = softmax(a2)
		
		return y
			
	#x：入力データ、y:教師データ
	# 損失関数（交差エントロピー）を計算する
	def loss (self, x, t):
		y = self.predict(x)
		loss = cross_entropy_error(y, t)
		return loss

	def accuracy(self, x, t):
		y = predict(x)
		y = np.argmax(y, axis=1)
		t = np.argmax(t, axis=1)
		
		accuracy = np.sum(y == t) / float(x.shape[0])
		return accuracy
		
	def numerical_gradient(self, x, t):
		loss_W = lambda W: self.loss(x, t)
		
		grads = {}
		grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
		grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
		grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
		grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
		
		return grads
		
	
	
		