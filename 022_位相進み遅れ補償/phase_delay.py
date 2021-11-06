"""
2021/04/03
@Yuya Shimizu

位相遅れ補償
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, bode
from control.matlab import logspace
from for_plot import bodeplot_set


#位相遅れ補償
alpha = 10      #α
T1 = 0.1        #時定数
K1 = tf([alpha*T1, alpha], [alpha*T1, 1])       #伝達関数
gain, phase, w = bode(K1, logspace(-2, 3), Plot=False)  #ゲイン，位相，周波数

#描画
fig, ax = plt.subplots(2, 1)
ax[0].semilogx(w, 20*np.log10(gain))    #ゲイン線図
ax[1].semilogx(w, phase*180/np.pi)      #位相線図
bodeplot_set(ax)
ax[0].set_title(f"Phase Delay Compensation; α={alpha}, $T_1$={T1}")

plt.show()
