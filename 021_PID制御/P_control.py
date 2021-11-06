"""
2021/03/26
@Yuya Shimzu

P制御（アーム）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, feedback
from control.matlab import bode, logspace, margin
from tf_arm import arm_tf       #自作関数
#https://qiita.com/Yuya-Shimizu/items/c7b69b4dfd63fb8facfa
from for_plot import linestyle_generator, plot_set, bodeplot_set      #自作関数
#https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623

##パラメータ設定
g    =   9.81                  #重力加速度[m/s^2]
l     =   0.2                    #アームの長さ[m]
M   =   0.5                    #アームの質量[kg]
mu =   1.5e-2               #粘性摩擦係数[kg*m^2/s]
J    =   1.0e-2               #慣性モーメント[kg*m^2]

#制御対象
P = arm_tf(J, mu, M, g, l)

#目標値(指示値=refference)
ref = 30        #目標角度30[deg]

#比例ゲイン
kp = (0.5, 1, 2)        #比較のために3つ用意



##P制御を用いたときのステップ応答の描画
LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)
for i in range(len(kp)):
    K = tf([0, kp[i]], [0, 1])  #P制御
    H = P*K  #開ループ系
    gain, phase, w = bode(H, logspace(-1, 2), Plot = False)     #ボード線図

    #ゲイン線図と位相線図
    pltargs = {'ls':next(LS), 'label':f"$k_P$={kp[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase*180/np.pi, **pltargs)
    
    #ゲイン余裕，位相余裕，位相交差周波数，ゲイン交差周波数
    print('Kp=', kp[i])
    print('(GM, PM, wpc, wgc)')
    print(margin(H))
    print('--------------------------')
    

ax[0].set_title('P control - Bode Plot')
bodeplot_set(ax, 3)

plt.show()

