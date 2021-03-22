"""
2021/02/11
@Yuya Shimizu

Matplotlibについての簡単なまとめ
"""
from matplotlib import pyplot as plt

import numpy as np

##グラフ作成
#データの準備
x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)

#描画
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


##オブジェクト指向のグラフ作成
"""先ほどの作成では，グラフを細部までカスタマイズして，よりきれいなグラフを作る時には不十分"""
#FigureとAxesオブジェクトの作成
fig, ax = plt.subplots()

#Axesオブジェクトの中にグラフを作成
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
fig.show()


##複数の図を比較描画
#2行1列という形で図の配置レイアウトを指定して，FigureとAxesオブジェクトを作成
fig, ax = plt.subplots(2, 1)

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
w = y + z

#1つ目のグラフを作成
ax[0].plot(x, y, linestyle = '-', label = 'sin', color = 'k')
ax[0].plot(x, z, linestyle = '-.', label = 'cos', color = 'k')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_xlim(0, 4*np.pi)
ax[0].grid()
ax[0].legend()

#2つ目のグラフを作成
ax[1].plot(x, w, color = 'k', marker = '.')
ax[1].set_xlabel('x')
ax[1].set_ylabel('w')
ax[1].set_xlim(0, 4*np.pi)
ax[1].grid(linestyle = ':')

#グラフが重なりすぎないようにする
fig.tight_layout()
fig.show()


##図を保存
fig.savefig('fig1.pdf')
