"""
2021/03/11
@Yuya Shimzu

PID制御と2自由度制御の比較{PI-D・I-PD制御}（アーム）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, feedback
from control.matlab import lsim
from tf_arm import arm_tf       #自作関数
#https://qiita.com/Yuya-Shimizu/items/c7b69b4dfd63fb8facfa
from for_plot import plot_set     #自作関数
#https://qiita.com/Yuya-Shimizu/items/f811317d733ee3f45623

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

#比例・積分・微分ゲイン
kp = 2
ki = 10
kd = 0.1

K1 = tf([kd, kp, ki], [1, 0])   #PID制御器
K2 = [tf([kp, ki], [kd, kp, ki]),   #PI-D制御の目標値整形フィードフォワード制御器
          tf([ki], [kd, kp, ki])]

#zからyへの伝達関数
Gyz = feedback(P*K1, 1)

Td = np.arange(0, 2, 0.01)
r = 1*(Td>0)


##PID制御とPI-D制御
#目標値rをK2で整形
z, t, _ = lsim(K2[0], r, Td, 0)

#PID制御(z=rとした場合)
y1, _, _ = lsim(Gyz, r, Td, 0)

#描画（PID制御）
fig, ax = plt.subplots(1, 2)
ax[0].plot(t, r*ref, color = 'k')   #入力信号の様子
ax[1].plot(t, y1*ref, ls = '--', label = 'PID', color = 'k')   #応答信号の様子

#PI-D制御
y2, _, _ = lsim(Gyz, z, Td, 0)

#描画（PI-D制御）
ax[0].plot(t, z*ref)   #入力信号の様子
ax[1].plot(t, y2*ref, label = 'PI-D')   #応答信号の様子

ax[0].set_title(f"INPUT  PID vs PI-D: $k_P$={kp}  $k_I$={ki}  $k_D$={kd}")
ax[1].set_title(f"OUTPUT  PID vs PI-D: $k_P$={kp}  $k_I$={ki}  $k_D$={kd}")
ax[1].axhline(ref, color='k', linewidth=0.5)
plot_set(ax[0], 't', 'r')
plot_set(ax[1], 't', 'y', 'best')

plt.show()


##PID制御とI-PD制御
#目標値rをK2で整形
z, t, _ = lsim(K2[1], r, Td, 0)

#描画（PID制御）
fig, ax = plt.subplots(1, 2)
ax[0].plot(t, r*ref, color = 'k')   #入力信号の様子
ax[1].plot(t, y1*ref, ls = '--', label = 'PID', color = 'k')   #応答信号の様子

#I-PD制御
y2, _, _ = lsim(Gyz, z, Td, 0)

#描画（I-PD制御）
ax[0].plot(t, z*ref)   #入力信号の様子
ax[1].plot(t, y2*ref, label = 'I-PD')   #応答信号の様子

ax[0].set_title(f"INPUT  PID vs I-PD: $k_P$={kp}  $k_I$={ki}  $k_D$={kd}")
ax[1].set_title(f"OUTPUT  PID vs I-PD: $k_P$={kp}  $k_I$={ki}  $k_D$={kd}")
ax[1].axhline(ref, color='k', linewidth=0.5)
plot_set(ax[0], 't', 'r')
plot_set(ax[1], 't', 'y', 'best')

plt.show()
