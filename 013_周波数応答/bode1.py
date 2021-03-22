"""
2021/03/07
@Yuya Shimizu

ボード線図（1次遅れ系）
"""
from control import tf, bode
from control.matlab import lsim, logspace
import matplotlib.pyplot as plt
import numpy as np
from for_plot import linestyle_generator, bodeplot_set      #自分で定義した関数をインポート
#定義した関数について (https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623)

K = 1
T = [1, 0.5, 0.1]   #時定数

LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)

for i in range(len(T)):
    P = tf([0, K], [T[i], 1])   #1次遅れ系

    #ゲイン，位相，周波数の取得　※Plot=Falseとすることで，値だけ取得し図は出力しない
    gain, phase, w = bode(P, logspace(-2, 2), Plot=False)

    #ボード線図をプロット
    plt_args = {'ls':next(LS), 'label': f"T={T[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **plt_args)    #.semilogxでx軸に対数表現を置いた片側対数グラフにプロット
    ax[1].semilogx(w, phase*180/np.pi, **plt_args)      #度数表現

ax[0].set_title("First-order delay system")
bodeplot_set(ax, 3, 3)
plt.show()
