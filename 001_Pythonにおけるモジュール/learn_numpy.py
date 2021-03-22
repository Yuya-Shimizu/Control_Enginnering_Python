"""
2021/02/10
@Yuya Shimizu

Numpyについての簡単なまとめ
"""

import numpy as np

##基本的な数値計算

#平方根
Sqrt = np.sqrt(4)
print(f"<平方根>\n{Sqrt}\n")

#絶対値
Abs = np.abs(-5)
print(f"<絶対値>\n{Abs}\n")

#三角関数
deg = 30
rad = np.deg2rad(deg)
Sin = np.sin(rad)
Cos = np.cos(rad)
Tan = np.tan(rad)
Arcsin = np.arcsin(Sin)
Arccos = np.arccos(Cos)
print(f"<三角関数>\ndeg = {deg} → rad = {rad}\nsin = {Sin}\ncos = {Cos}\ntan = {Tan}\narcsin = {Arcsin}\narccos = {Arccos}\n")

#指数
Exp = np.exp(1)
print(f"<指数>\n{Exp}\n")

#対数
Nlog = np.log(Exp)
Log = np.log10(10)
print(f"<対数>\n{Nlog}(自然対数)\n{Log}(常用対数)\n")

#四捨五入
Round = np.round(5.55)
print(f"<四捨五入>\n{Round}\n")

#円周率
Pi = np.pi
print(f"<円周率>\n{Pi}\n")

#複素数
Con = -5+2j
Conj = np.conj(Con)
Real = np.real(Con)
Imaginary = np.imag(Con)
print(f"<複素数>\n{Con}\n共役な複素数: {Conj}\n実部: {Real}\n虚部: {Imaginary}\n")


##ベクトルや行列の演算

#定義
A = np.array([[1, 2],
                     [-3, 4]
                    ])
print(f"<行列(ベクトル)の定義>\n{A}\n")

#転置
Trans = A.T
print(f"<転置>\n{Trans}\n")

#逆行列
Inverse = np.linalg.inv(A)
print(f"<逆行列>\n{Inverse}\n")

#行列式
Determinant = np.linalg.det(A)
print(f"<行列式>\n{Determinant}\n")

#ランク(階数)
Rank = np.linalg.matrix_rank(A)
print(f"<ランク(階数)>\n{Rank}\n")

#固有値と固有ベクトル
w, v = np.linalg.eig(A)
print(f"<固有値と固有ベクトル>\neigenvalue = {w}\neigenvector = \n{v}\n")

#ノルム
x = np.array([1, 2])
Norm = np.linalg.norm(x)
print(f"<ノルム>\n{Norm}\n")

#数列の作成
Numerical_sequence = np.arange(0, 10, 1)
print(f"<数列の作成>\n{Numerical_sequence}\n")
