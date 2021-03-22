"""
2021/03/21
@Yuya Shimizu

状態フィードバック制御（外乱あり）
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
C = [[ 1, 0],
        [ 0, 1]]
D = [[0],
        [0]]

P = ss(A, B, C, D)

##極配置法
Pole = [-1, -1]
F = -acker(P.A, P.B, Pole)

##状態フィードバック制御
Acl = P.A + P.B*F   #入力をFとする
Pfb = ss(Acl, P.B, P.C, P.D)    #状態フィードバックで安定化したシステム

Td = np.arange(0, 8, 0.01)  #シミュレーション時間
Ud = 0.2 * (Td>0)   #ステップ状の外乱
x0 = [-0.3, 0.4]    #初期状態
x, t, _ = lsim(Pfb, Ud, Td, x0)

#描画
fig, ax = plt.subplots()
ax.plot(t, x[:, 0], label = '$x_1$')
ax.plot(t, x[:, 1], ls = '-.', label = '$x_2$')
ax.set_title('response of state - with disturbance')
plot_set(ax, 't', 'x', 'best')
plt.show()
