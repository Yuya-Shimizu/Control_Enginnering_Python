"""
2021/03/17
@Yuya Shimizu

kp, ki, kdを求める
"""
import sympy as sp

#文字の定義
z, wn = sp.symbols('zeta omega_n')
a1, a2 = sp.symbols('alpha1 alpha2')
kp, kd, ki = sp.symbols('k_p k_d k_i')
Mgl, mu, J = sp.symbols('Mgl mu J')
sp.init_printing()
         
solution = {}   #結果を格納する辞書型配列

#PI-D & 2-dimention
f1 = Mgl/ki - 2*z/wn
f2 = (mu+kd)/ki - Mgl*kp/(ki**2) - 1/(wn**2)
f3 = J/ki - kp*(mu+kd)/(ki**2) + Mgl*kp**2/(ki**3)
solution['PI-D & 2-dimention'] = sp.solve([f1, f2, f3], [kp, kd, ki])

#PI-D & 3-dimention
f1 = Mgl/ki - a1/wn
f2 = (mu+kd)/ki - Mgl*kp/(ki**2) - a2/(wn**2)
f3 = J/ki - kp*(mu+kd)/(ki**2) + Mgl*kp**2/(ki**3) - 1/(wn**3)
solution['PI-D & 3-dimention'] = sp.solve([f1, f2, f3], [kp, kd, ki])

#I-PD & 2-dimention
f1 = (Mgl+kp)/ki - 2*z/wn
f2 = (mu+kd)/ki - 1/(wn**2)
f3 = J/ki
solution['I-PD & 2-dimention'] = sp.solve([f1, f2, f3], [kp, kd, ki])

#I-PD & 3-dimention
f1 = (Mgl+kp)/ki - a1/wn
f2 = (mu+kd)/ki - a2/(wn**2)
f3 = J/ki  - 1/(wn**3)

solution['I-PD & 3-dimention'] = sp.solve([f1, f2, f3], [kp, kd, ki])

for S in solution:
    print(f"<{S}>\n{solution[S]}\n\n")
