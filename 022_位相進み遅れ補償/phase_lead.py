"""
2021/04/03
@Yuya Shimizu

位相進み補償
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, bode
from control.matlab import logspace
from for_plot import bodeplot_set


#位相遅れ補償
beta = 0.1      #β
T2 = 1        #時定数
K2 = tf([T2, 1], [beta*T2, 1])       #伝達関数
gain, phase, w = bode(K2, logspace(-2, 3), Plot=False)  #ゲイン，位相，周波数

#描画
fig, ax = plt.subplots(2, 1)
ax[0].semilogx(w, 20*np.log10(gain))    #ゲイン線図
ax[1].semilogx(w, phase*180/np.pi)      #位相線図
bodeplot_set(ax)
ax[0].set_title(f"Phase Lead Compensation; β={beta}, $T_2$={T2}")

plt.show()
