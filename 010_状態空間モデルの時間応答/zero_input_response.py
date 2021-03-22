"""
2021/03/02
@Yuya Shimizu

状態空間モデルの初期値応答
"""
import numpy as np
from control import  ss
from control.matlab import  initial
from for_plot import *
import matplotlib.pyplot as plt

##状態空間モデルの設定
A = [[ 0,  1],
       [-4, -5]]

B = [[0],
        [1]]

C = [[ 1, 0],
       [ 0, 1]]     #np.eye(2)とも記述できる

D = [[0],
        [0]]        #np.zeros([2,1])とも記述できる

P = ss(A, B, C, D)


##初期値応答
Td = np.arange(0, 5, 0.01)    #シミュレーション時間
x0 = [-0.3, 0.4]                    #初期値
x, t = initial(P, Td, x0)           #初期値応答（零入力応答）


##描画
fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label = '$x_1$')
ax.plot(t, x[:, 1], ls = '-.', label = '$x_2$')
ax.set_title('zero input response')
plot_set(ax, 't', 'x', 'best')
plt.show()
