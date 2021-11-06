"""
2021/04/03
@Yuya Shimizu

垂直駆動アームの制御系設計
（ゲイン補償・位相遅れ補償・位相進み補償）
K(s) = kK1(s)K2(s)

[設計仕様]
・ゲイン交差周波数：40 rad/s
・位相余裕：60 deg
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, bode, feedback
from control.matlab import logspace, freqresp, margin, step
from for_plot import bodeplot_set, plot_set       #自作関数
from tf_arm import arm_tf       #自作関数

###制御対象（垂直アーム）
#パラメータ設定
g    =   9.8                    #重力加速度[m/s^2]
l     =   0.2                    #アームの長さ[m]
M   =   0.5                     #アームの質量[kg]
mu =   1.5e-2                #粘性摩擦係数[kg*m^2/s]
J    =   1.0e-2                 #慣性モーメント[kg*m^2]

#目標値
ref = 30

#制御モデル
P = arm_tf(J, mu, M, g, l)


############## 制御系設計開始 ##############

###位相遅れ補償により低周波ゲインを大きくする
#位相遅れ補償
alpha = 20      #α
T1 = 0.25        #時定数
K1 = tf([alpha*T1, alpha], [alpha*T1, 1])       #補償器

#開ループ系
H1 = P * K1

gain, phase, w = bode(H1, logspace(-1, 2), Plot=False)  #ゲイン，位相，周波数

#描画
fig, ax = plt.subplots(2, 1)
ax[0].semilogx(w, 20*np.log10(gain))    #ゲイン線図
ax[1].semilogx(w, phase*180/np.pi)      #位相線図
bodeplot_set(ax)
ax[0].set_title(f"Phase Delay Compensation; α={alpha}, $T_1$={T1}")

plt.show()

#40 radに置けるゲインと位相を確認
[[[mag]]], [[[phase]]], omega = freqresp(H1, [40])
magH1at40 = mag
phaseH1at40 = phase * (180/np.pi)
print('-'*20)
print(f"phase at 40 rad/s = {phaseH1at40}")


###位相進み補償により位相余裕が望みのものになるように位相を進ませる
#位相進み補償
phi_m = (60-(180 + phaseH1at40)) * np.pi/180
beta = (1 - np.sin(phi_m))/(1 + np.sin(phi_m))      #β
T2 = 1/40/np.sqrt(beta)        #時定数
K2 = tf([T2, 1], [beta*T2, 1])       #補償器

#開ループ系
H2 = P * K1 * K2

gain, phase, w = bode(H2, logspace(-1, 2), Plot=False)  #ゲイン，位相，周波数

#描画
fig, ax = plt.subplots(2, 1)
ax[0].semilogx(w, 20*np.log10(gain))    #ゲイン線図
ax[1].semilogx(w, phase*180/np.pi)      #位相線図
bodeplot_set(ax)
ax[0].set_title(f"PDC & PLC; α={alpha}, β={beta:.5f}, $T_1$={T1}, $T_2$={T2:.5f}")

plt.show()

#40 radに置けるゲインと位相を確認
[[[mag]]], [[[phase]]], omega = freqresp(H2, [40])
magH2at40 = mag
gainH2at40 = 20 * np.log10(magH2at40)
phaseH2at40 = phase * (180/np.pi)
print('-'*20)
print(f"gain at 40 rad/s = {gainH2at40}")
print(f"phase at 40 rad/s = {phaseH2at40}")


###ゲイン補償の設計とループ整形の結果
#ゲイン補償
k = 1/magH2at40 #H2の40 radにおけるゲインを0 dBに持っていくようにゲイン補償を設計

##開ループ系（設計後）
H = P * k * K1 * K2

gain, phase, w = bode(H, logspace(-1, 2), Plot=False)  #ゲイン，位相，周波数

#描画
fig, ax = plt.subplots(2, 1)
ax[0].semilogx(w, 20*np.log10(gain), label='H')    #ゲイン線図
ax[1].semilogx(w, phase*180/np.pi, label='H')      #位相線図
bodeplot_set(ax, 3)


##開ループ系P（設計後）
gain, phase, w = bode(P, logspace(-1, 2), Plot=False)  #ゲイン，位相，周波数

#描画
ax[0].semilogx(w, 20*np.log10(gain), ls = '--', label='P')    #ゲイン線図
ax[1].semilogx(w, phase*180/np.pi, ls = '--', label='P')      #位相線図
bodeplot_set(ax, 3)
ax[0].set_title(f"k & PDC & PLC; k={k:.5f}, α={alpha}, β={beta:.5f}, $T_1$={T1}, $T_2$={T2:.5f}")

plt.show()

# ゲイン余裕，位相余裕，位相交差周波数，ゲイン交差周波数
print('-'*20)
print('(GM, PM, wpc, wgc)')
print(margin(H))

############## 制御系設計終了 ##############

############## ループ整形前後での確認 ##############
##ステップ応答
fig, ax = plt.subplots()

#設計後の閉ループ系のステップ応答
Gyr_H = feedback(H, 1)
y, t = step(Gyr_H, np.arange(0, 2, 0.01))
ax.plot(t, y*ref, label = 'After')

#設計前の閉ループ系のステップ応答
Gyr_P = feedback(P, 1)
y, t = step(Gyr_P, np.arange(0, 2, 0.01))
ax.plot(t, y*ref, ls = '--', label = 'Before')

ax.axhline(ref, color = 'r', linewidth = 0.5)   #目標値
plot_set(ax, 't', 'y', 'best')
ax.set_title(f"Comparison Before v.s. After 'loop shaping' at closed loop")

plt.show()

##ボード線図
fig, ax = plt.subplots(2, 1)

#設計後の閉ループ系のボード線図
gain, phase, w = bode(Gyr_H, logspace(-1, 2), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), label = 'After')
ax[1].semilogx(w, phase*180/np.pi, label = 'After')

#設計前の閉ループ系のボード線図
gain, phase, w = bode(Gyr_P, logspace(-1, 2), Plot = False)
ax[0].semilogx(w, 20*np.log10(gain), ls = '--', label = 'Before')
ax[1].semilogx(w, phase*180/np.pi, ls = '--', label = 'Before')

bodeplot_set(ax, 3)
ax[0].set_title(f"Comparison Before v.s. After 'loop shaping' at closed loop")

plt.show()
