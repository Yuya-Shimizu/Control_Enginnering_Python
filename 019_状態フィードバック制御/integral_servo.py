"""
2021/03/21
@Yuya Shimizu

積分型サーボ系（外乱あり）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import ss
from control.matlab import acker, lsim
from for_plot import plot_set

##状態空間モデル
A = [[ 0, 1],
        [-4, 5]]
B = [[0],
        [1]]
C = [1, 0]
D = [0]

P = ss(A, B, C, D)

#拡大系
Ae1 = np.c_[P.A, np.zeros((2, 1))]
Ae = np.r_[Ae1, -np.c_[P.C, 0]]
Be = np.c_[P.B.T, 0].T
Ce = np.c_[P.C, 0]

##拡大系に対する極配置法
Pole = [-1, -1, -5]
Fe = -acker(Ae, Be, Pole)  #Fe: 拡大系に対するフィードバックゲイン

##閉ループ系
Acl = Ae + Be*Fe   #入力をFとする
Pfb = ss(Acl, Be, np.eye(3), np.zeros((3, 1)))

Td = np.arange(0, 8, 0.01)  #シミュレーション時間
Ud = 0.2 * (Td>0)   #ステップ状の外乱
x0 = [-0.3, 0.4, 0]    #初期状態
x, t, _ = lsim(Pfb, Ud, Td, x0)

#描画
fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label = '$x_1$')
ax.plot(t, x[:, 1], ls = '-.', label = '$x_2$')
ax.set_title('response of state - integral servo')
plot_set(ax, 't', 'x', 'best')
plt.show()
