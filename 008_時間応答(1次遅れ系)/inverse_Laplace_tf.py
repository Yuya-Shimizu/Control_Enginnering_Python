"""
2021/02/26
@Yuya Shimizu

逆ラプラス変換
"""

import sympy as sp

sp.init_printing()
s = sp.Symbol('s')
t = sp.Symbol('t', positive=True)
T = sp.Symbol('T', real=True)
P = 1/((1 + T*s)*s)

Inverse = sp.inverse_laplace_transform(1/s - 1/(s+1/T), s, t)   #逆ラプラス変換

print(f"1/s - 1/(s+1/T)\n     ↓\n{Inverse}")
