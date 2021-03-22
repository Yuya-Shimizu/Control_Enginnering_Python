"""
2021/02/26
@Yuya Shimizu

部分分数分解
"""

import sympy as sp

sp.init_printing()
s = sp.Symbol('s')
T = sp.Symbol('T', real=True)
P = 1/((1 + T*s)*s)

Apart = sp.apart(P, s)#部分分数分解

print(f"{P}\n     ↓\n{Apart}")
