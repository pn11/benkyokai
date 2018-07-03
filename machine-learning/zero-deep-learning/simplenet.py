# coding : utf-8

import sys, os
#sys.path append(os.pardir) #　親ディレクトリをPATHに追加
import numpy as np

from functions import softmax, cross_entropy_error
from gradient import numerical_gradient

class simpleNet:
	def __init__(self):
		self.W = np.random.randn(2, 3) # 重みをガウシアンで初期化
	
	def predict(self, x):
		return np.dot(x, self.W) # 入力データに重みをかける
		
	def loss (self, x, t): # 損失関数（交差エントロピー）を計算する
		z = self.predict(x)
		y = softmax(z)
		loss = cross_entropy_error(y, t)
		
		return loss
