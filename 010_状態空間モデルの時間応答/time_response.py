"""
2021/03/02
@Yuya Shimizu

状態空間モデルの時間応答
"""
import numpy as np
from control import  ss
from control.matlab import  initial, step, lsim
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


##時間応答 (=零入力応答 + 零状態応答)
Td = np.arange(0, 5, 0.01)    #シミュレーション時間
Ud = 1*(Td>0)
x0 = [-0.3, 0.4]            #初期値

xst, t = step(P, Td)           #零状態応答
xin, _ = initial(P, Td, x0)   #零入力応答
x, _, _ = lsim(P, Ud, Td, x0)   #時間応答

##描画
fig, ax = plt.subplots(1, 2, figsize=(6, 2.3))

for i in [0, 1]:
    ax[i].plot(t, x[:, i], label = 'time response')             #時間応答の描画
    ax[i].plot(t, xst[:, i], ls = '--', label = 'zero state')    #零状態応答の描画
    ax[i].plot(t, xin[:, i], ls = '-.', label = 'zero input')    #零入力応答の描画

ax[0].set_title('response for $x_1$')
ax[1].set_title('response for $x_2$')
plot_set(ax[0], 't', '$x_1$')
plot_set(ax[1], 't', '$x_2$', 'best')
fig.tight_layout()
plt.show()

