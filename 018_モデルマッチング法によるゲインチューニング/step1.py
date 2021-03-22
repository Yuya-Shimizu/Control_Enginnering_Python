"""
2021/03/17
@Yuya Shimizu

マクローリン展開
"""
import sympy as sp

#文字の定義
s = sp.Symbol('s')
kp, kd, ki = sp.symbols('k_p k_d kj_i')
Mgl, mu, J = sp.symbols('Mgl mu J')
sp.init_printing()

Mc = {} #結果を格納する辞書型配列

#PI-D
G = (kp*s+ki)/(J*s**3 + (mu+kd)*s**2 + (Mgl+kp)*s +ki)
Mc['PI-D'] = sp.series(1/G, s, 0, 4)    #3次の項まで展開

#I-PD
G = (ki)/(J*s**3 + (mu+kd)*s**2 + (Mgl+kp)*s +ki)
Mc['I-PD'] = sp.series(1/G, s, 0, 4)    #3次の項まで展開

for M in Mc:
    print(f"<{M}>\n{Mc[M]}\n\n")
