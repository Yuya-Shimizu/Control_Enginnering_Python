"""
2021/03/15
@Yuya Shimzu

PIDゲインチューニング：限界感度法（アーム）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, feedback
from control.matlab import pade, step
from tf_arm import arm_tf       #自作関数
#https://qiita.com/Yuya-Shimizu/items/c7b69b4dfd63fb8facfa
from for_plot import plot_set, linestyle_generator     #自作関数
#https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623

simT = np.arange(0, 2, 0.01)    #シミュレーション時間

##パラメータ設定
g    =   9.8                    #重力加速度[m/s^2]
l     =   0.2                    #アームの長さ[m]
M   =   0.5                     #アームの質量[kg]
mu =   1.5e-2                #粘性摩擦係数[kg*m^2/s]
J    =   1.0e-2                 #慣性モーメント[kg*m^2]

#制御対象
P = arm_tf(J, mu, M, g, l)

#目標値(指示値=refference)
ref = 30        #目標角度30[deg]

#むだ時間
num_delay, den_delay = pade(0.005, 1)   #1次のパデ近似（むだ時間：0.005）

#むだ時間を考慮した制御対象
P_delay = P * tf(num_delay, den_delay)


#####限界感度法
###手順①
#持続振動が生じる適当な初期ゲインを設定
fig, ax = plt.subplots()

kp0 = 2.9   #今回の場合，2.9辺りで持続振動が生じる
K = tf([0, kp0], [0, 1])
Gyr = feedback(P_delay*K, 1)
y, t = step(Gyr, simT)

ax.plot(t, y*ref)
ax.axhline(ref, color = 'r', linewidth = 0.5)
ax.set_title("step1; $k_{P0}$="+str(kp0))
plot_set(ax, 't', 'y')
plt.show()

#持続振動が生じるグラフにおける周期T0を得る
#上で描かれるグラフからは，T0はおよそ0.3と見積もれる
T0 = 0.3

###手順②
##各ゲインを計算
kp = [0, 0]
ki = [0, 0]
kd = [0, 0]
Rule = ['', '']

#限界感度法（Classic）
Rule[0] = 'Classic'
kp[0] = 0.6 * kp0
ki[0] = kp[0] / (0.5 * T0)
kd[0] = kp[0] * (0.125 * T0)

#改良された限界感度法（No overshoot）
Rule[1] = 'No Overshoot'
kp[1] = 0.2 * kp0
ki[1] = kp[1] / (0.5 * T0)
kd[1] = kp[1] * (0.33 * T0)

LS = linestyle_generator()
fig, ax = plt.subplots()

for i in range(len(Rule)):
    K = tf([kd[i], kp[i], ki[i]], [1, 0])
    Gyr = feedback(P_delay*K, 1)
    y, t = step(Gyr, simT)

    ax.plot(t, y*ref, ls=next(LS), label = f"{Rule[i]}; $k_P$ = {kp[i]}, $k_I$ = {ki[i]}, $k_D$ = {kd[i]}")

ax.axhline(ref, color = 'r', linewidth = 0.5)
ax.set_title("PID control")
plot_set(ax, 't', 'y', 'best')
plt.show()
