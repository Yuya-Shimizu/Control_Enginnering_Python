"""
2021/03/17
@Yuya Shimizu

モデルマッチング（2次規範モデル）- アームの角度制御
"""

import numpy as np
import matplotlib.pyplot as plt
from control import tf
from control.matlab import step
from for_plot import plot_set

#マッチング法を適用するクラス
class Matching():
    """P-IDかI-PDをGに，規範モデルの次元をdimに指定できる"""
    def __init__(self, G, dim):
        self.omega_n = 15
        if dim == 2:
            self.zeta = 0.707   #バターワース（二項係数標準形でも構わない）
        elif dim == 3:
            self.alpha = [3, 3] #二項係数標準形（他のでもよいがこれが性能がよかった）
        
        self.G = G
        self.dim = dim

        #パラメータ設定
        self.g    =   9.8                    #重力加速度[m/s^2]
        self.l     =   0.2                    #アームの長さ[m]
        self.M   =   0.5                     #アームの質量[kg]
        self. mu =   1.5e-2                #粘性摩擦係数[kg*m^2/s]
        self.J    =   1.0e-2                 #慣性モーメント[kg*m^2]
        #目標値(指示値=refference)
        self.ref = 30        #目標角度30[deg]

        ##実行
        self.model()
        self.matching()
        
    #規範モデル
    def model(self):
        if self.dim == 2:
            self.Msys = tf([0, self.omega_n**2], [1, 2*self.zeta*self.omega_n, self.omega_n**2])
        elif self.dim == 3:
            self.Msys = tf([0, self.omega_n**3], [1, self.alpha[1]*self.omega_n, self.alpha[0]*self.omega_n**2, self.omega_n**3])

    #モデルマッチング
    def matching(self):
        simT = np.arange(0, 2, 0.01)

        if self.G == 'PI-D':
            if self.dim == 2:
                kp = self.omega_n**2*self.J
                ki = self.omega_n*self.M*self.g*self.l/(2*self.zeta)
                kd = 2*self.zeta*self.omega_n*self.J + self.M*self.g*self.l/(2*self.zeta*self.omega_n) - self.mu
            elif self.dim == 3:
                kp = (self.J*self.alpha[0]*self.omega_n**2 - self.M*self.g*self.l)/(self.alpha[0]*self.alpha[1])
                ki = self.M*self.g*self.l*self.omega_n/self.alpha[0]
                kd = self.J*self.alpha[0]*self.omega_n/self.alpha[1] - self.M*self.g*self.l/(self.alpha[1]*self.omega_n) + self.M*self.g*self.l*self.alpha[1]/(self.alpha[0]*self.omega_n) - self.mu
            else:
                print(f"can't calculate kp, ki, kd by matching with {self.dim}-dim model")
                return

            Gyr = tf([kp, ki], [self.J, self.mu+kd, self.M*self.g*self.l+kp, ki])

        elif self.G == 'I-PD':
            if self.dim == 3:
                kp = self.J*self.alpha[0]*self.omega_n**2 - self.M*self.g*self.l
                ki = self.J*self.omega_n**3
                kd = self.J*self.alpha[1]*self.omega_n - self.mu
            else:
                print(f"can't calculate kp, ki, kd by matching with {self.dim}-dim model")
                return

            Gyr = tf([0, ki], [self.J, self.mu+kd, self.M*self.g*self.l+kp, ki])

        #シミュレーション
        yM, tM = step(self.Msys, simT)
        y, t = step(Gyr, simT)

        #描画
        fig, ax = plt.subplots()
        ax.plot(tM, yM*self.ref, label = 'M')
        ax.plot(t, y*self.ref, label = 'Gyr')
        plot_set(ax, 't', 'y', 'best')
        ax.set_title(f"{self.G} & {self.dim}-dimention model")

        plt.show()

if __name__=='__main__':
    Match = Matching('PI-D', 2) #PI-D, 2-dimention
    Match = Matching('PI-D', 3) #PI-D, 3-dimention
    Match = Matching('I-PD', 2) #I-PD, 2-dimention
    Match = Matching('I-PD', 3) #I-PD, 3-dimention
    
