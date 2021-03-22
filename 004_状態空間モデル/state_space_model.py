"""
2021/02/20
@Yuya Shimizu

状態空間モデル
"""
from control import ss, ssdata

##ss関数では，MATLAB表記が可能

#状態空間モデル構築
A = '0 1; -1 -1'
B = '0 ; 1'
C = '1 0'
D = '0'

state_model  = ss(A, B, C, D)
print(f"<状態空間モデル>\n{state_model}\n")

#状態空間モデルからA~D行列の抽出
print("<定数行列A~D>")
print('A=', state_model.A)
print('B=', state_model.B)
print('C=', state_model.C)
print('D=', state_model.D)

#もしくは，以下の方法でまとめて抽出できる
sysA, sysB, sysC, sysD = ssdata(state_model)
