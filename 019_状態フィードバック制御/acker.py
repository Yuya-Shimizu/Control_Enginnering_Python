"""
2021/03/21
@Yuya Shimizu

状態フィードバック制御（極配置法）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import ss
from control.matlab import acker, initial
from for_plot import plot_set

##状態空間モデル
A = [[ 0, 1],
        [-4, 5]]
B = [[0],
        [1]]
C = [[ 1, 0],
        [ 0, 1]]
D = [[0],
        [0]]

P = ss(A, B, C, D)

##極配置法
Pole = [-1, -1] #望みの極を指定
F = -acker(P.A, P.B, Pole)  #アッカーマンの極配置アルゴリズムが実装された関数を使用

print(f"<結果>\nF={F}\n<結論>\nどうやらフィードバックゲインを{F}にすることで，極を{Pole}に配置できるようだ")

##状態フィードバック制御
Acl = P.A + P.B*F   #入力をFとする
Pfb = ss(Acl, P.B, P.C, P.D)    #状態フィードバック制御

Td = np.arange(0, 5, 0.01)  #シミュレーション時間
x0 = [-0.3, 0.4]    #初期状態
x, t = initial(Pfb, Td, x0)

#描画
fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label = '$x_1$')
ax.plot(t, x[:, 1], ls = '-.', label = '$x_2$')
ax.set_title('response of state - pole placement method')
plot_set(ax, 't', 'x', 'best')
plt.show()
