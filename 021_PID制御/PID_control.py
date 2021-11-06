"""
2021/03/28
@Yuya Shimzu

PID制御（アーム）
"""
import numpy as np
import matplotlib.pyplot as plt
from control import tf, feedback
from control.matlab import step, bode, logspace, margin
from tf_arm import arm_tf       #自作関数
#https://qiita.com/Yuya-Shimizu/items/c7b69b4dfd63fb8facfa
from for_plot import linestyle_generator, plot_set, bodeplot_set      #自作関数
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

#比例ゲイン・積分ゲイン・微分ゲイン
kp = 2
ki = 5
kd = (0, 0.1, 0.2)        #比較のために3つ用意


##PID制御を用いたときのボード線図（開ループ系）
LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)
for i in range(len(kd)):
    K = tf([kd[i], kp, ki], [1, 0])  #PID制御
    H = P * K  #開ループ系
    gain, phase, w = bode(H, logspace(-1, 2), Plot=False)     #ボード線図

    #ゲイン線図と位相線図
    pltargs = {'ls':next(LS), 'label':f"$k_D$={kd[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase*180/np.pi, **pltargs)
    
    #ゲイン余裕，位相余裕，位相交差周波数，ゲイン交差周波数
    print('Kp=', kp, 'Ki=', ki, 'Kd=', kd[i])
    print('(GM, PM, wpc, wgc)')
    print(margin(H))
    print('--------------------------')
    
ax[0].set_title(f"PID control : $k_P$={kp} $k_I$={ki} $k_D$={kd} - Bode Plot")
bodeplot_set(ax, 'lower left')

plt.show()


##PID制御を用いたときのステップ応答の描画（閉ループ系）
LS = linestyle_generator()
fig, ax = plt.subplots()
for i in range(len(kd)):
    K = tf([kd[i], kp, ki], [1, 0])  #PID制御
    Gyr = feedback(P*K, 1)  #閉ループ系
    y, t = step(Gyr, np.arange(0, 2, 0.01))     #ステップ応答

    pltargs = {'ls':next(LS), 'label':f"$k_D$={kd[i]}"}
    ax.plot(t, y*ref, **pltargs)

ax.set_title(f"PID control: $k_P$={kp}  $k_I$={ki}  $k_D$={kd}")
ax.axhline(ref, color='k', linewidth=0.5)
plot_set(ax, 't', 'y', 'best')

plt.show()



#比例ゲイン・積分ゲイン・微分ゲイン
kp = (2, 1)
ki = (5, 0)
kd = (0.1, 0)        #比較のために3つ用意

Label = ('After', 'Before')
##PID制御を用いたときのボード線図の描画（開ループ系）- 設計の前後
LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)
for i in range(len(Label)):
    K = tf([kd[i], kp[i], ki[i]], [1, 0])  #PID制御
    H = P * K  #開ループ系
    gain, phase, w = bode(H, logspace(-1, 2), Plot=False)     #ボード線図

    #ゲイン線図と位相線図
    pltargs = {'ls':next(LS), 'label':f"{Label[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase*180/np.pi, **pltargs)

    
ax[0].set_title(f"PID control : $k_P$={kp} $k_I$={ki} $k_D$={kd} - Bode Plot")
bodeplot_set(ax, 'lower left')

plt.show()


##PID制御を用いたときのボード線図の描画（閉ループ系）- 設計の前後
LS = linestyle_generator()
fig, ax = plt.subplots(2, 1)
for i in range(len(Label)):
    K = tf([kd[i], kp[i], ki[i]], [1, 0])  #PID制御
    Gyr = feedback(P * K, 1)  #閉ループ系
    gain, phase, w = bode(Gyr, logspace(-1, 2), Plot=False)     #ボード線図

    #ゲイン線図と位相線図
    pltargs = {'ls':next(LS), 'label':f"{Label[i]}"}
    ax[0].semilogx(w, 20*np.log10(gain), **pltargs)
    ax[1].semilogx(w, phase*180/np.pi, **pltargs)
    
ax[0].set_title(f"PID control : $k_P$={kp} $k_I$={ki} $k_D$={kd} - Bode Plot")
bodeplot_set(ax, 'lower left')

plt.show()

##PID制御を用いたときのステップ応答の描画（閉ループ系）- 設計の前後
LS = linestyle_generator()
fig, ax = plt.subplots()
for i in range(len(kd)):
    K = tf([kd[i], kp[i], ki[i]], [1, 0])  #PID制御
    Gyr = feedback(P*K, 1)  #閉ループ系
    y, t = step(Gyr, np.arange(0, 2, 0.01))     #ステップ応答

    pltargs = {'ls':next(LS), 'label':f"{Label[i]}"}
    ax.plot(t, y*ref, **pltargs)

ax.set_title(f"PID control: $k_P$={kp}  $k_I$={ki}  $k_D$={kd}")
ax.axhline(ref, color='k', linewidth=0.5)
plot_set(ax, 't', 'y', 'best')

plt.show()
