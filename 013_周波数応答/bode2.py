"""
2021/03/07
@Yuya Shimizu

ボード線図（2次遅れ系）
"""
from control import tf, bode
from control.matlab import lsim, logspace
import matplotlib.pyplot as plt
import numpy as np
from for_plot import linestyle_generator, bodeplot_set     #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)


##減衰係数の変化によるボード線図の違い
K = 1
zeta = [1, 0.7, 0.4]   #減衰係数
omega_n = 5

LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)

for i in range(len(zeta)):
    P = tf([0, K*omega_n**2], [1, 2*zeta[i]*omega_n, omega_n**2])   #2次遅れ系

    #ゲイン，位相，周波数の取得　※Plot=Falseとすることで，値だけ取得し図は出力しない
    gain, phase, w = bode(P, logspace(-2, 2), Plot=False)

    #ボード線図をプロット
    plt_args = {'ls':next(LS), 'label': f"$\zeta$={zeta[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **plt_args)    #.semilogxでx軸に対数表現を置いた片側対数グラフにプロット
    ax[1].semilogx(w, phase*180/np.pi, **plt_args)      #度数表現

ax[0].set_title("Second-order delay system: changed $\zeta$")
bodeplot_set(ax, 3, 3)
plt.show()


##固有角振動数の変化によるボード線図の違い
K = 1
zeta = 0.7
omega_n = [1, 5, 10]    #固有角振動数

LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)

for i in range(len(omega_n)):
    P = tf([0, K*omega_n[i]**2], [1, 2*zeta*omega_n[i], omega_n[i]**2])   #2次遅れ系

    #ゲイン，位相，周波数の取得　※Plot=Falseとすることで，値だけ取得し図は出力しない
    gain, phase, w = bode(P, logspace(-2, 2), Plot=False)

    #ボード線図をプロット
    plt_args = {'ls':next(LS), 'label': f"$\omega_n$={omega_n[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **plt_args)    #.semilogxでx軸に対数表現を置いた片側対数グラフにプロット
    ax[1].semilogx(w, phase*180/np.pi, **plt_args)      #度数表現

ax[0].set_title("Second-order delay system: changed $\omega_n$")
bodeplot_set(ax, 3, 3)
plt.show()
