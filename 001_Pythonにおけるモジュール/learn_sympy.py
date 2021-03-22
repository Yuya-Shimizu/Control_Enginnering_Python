"""
2021/02/12
@Yuya Shimizu

Sympyについての簡単なまとめ
数式処理モジュール
変数を文字のまま扱い，さまざまな計算を行うことができる
(例)
式の展開や因数分解，微分，積分，ラプラス変換まで実行可能
"""

import sympy as sp

sp.init_printing()  #これを実行しておけば，LaTeX形式の出力が表示される

##数式処理

#方程式を解く
x = sp.Symbol('x')
root = sp.solve(2*x**2 + 5*x + 3, x)
print(f"<方程式を解く>\n2*x**2 + 5*x + 3 = 0\tx = {root}\n")

#式の展開
f = sp.expand((x+1)*(x+2)**2, x)
print(f"<式の展開>\n(x+1)*(x+2)**2 = {f}\n")

#因数分解
g = sp.factor(f, x)
print(f"<式の展開>\n{f} = {g}\n")

#テイラー展開
sin_t = sp.series(sp.sin(x), x)
cos_t = sp.series(sp.cos(x), x)
print(f"<テイラー展開>\nsin(x) = {sin_t}\n")
print(f"cos(x) = {cos_t}\n")

#部分分数分解
a = sp.apart(1/((5*x)*(x+1)))
print(f"<部分分数分解>\n1/((5*x)*(x+1)) = {a}\n")

#ラプラス変換
s, t = sp.symbols('s t')
w = sp.Symbol('w', real=True)   #real=Trueは必要でないと，逆ラプラス変換のときにおかしな表示となる
laplace = sp.laplace_transform(sp.sin(w * t), t, s)
print(f"<ラプラス変換>\nsin(s) = {laplace[0]}\n")

#逆ラプラス変換
inverse_laplace = sp.inverse_laplace_transform(laplace[0], s, t)
print(f"<逆ラプラス変換>\n{laplace[0]} = {inverse_laplace}\n")

