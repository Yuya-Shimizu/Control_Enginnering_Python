"""
2021/03/04
@Yuya Shimizu

漸近安定
"""
from for_plot import plot_set   #別ファイルに定義
from control import tf, pole
import matplotlib.pyplot as plt
import numpy as np

"""
##固有値の計算
A = np.array([[0, 1],
                     [-4, -5]])
eigenvalue = np.linalg.eigvals(A)
"""
print(f"<固有値の計算>\nA = {A}\t\tAの固有値  →  {eigenvalue}")

##位相図面

w = 1.5     #刻み幅の設定
Y, X = np.mgrid[-w:w:100j, -w:w:100j]

A = np.array([[0, 1],
                     [-4, -5]])
eig, vec = np.linalg.eig(A)     #行列Aの固有ベクトルvecと固有値eig

#dx/dt = Axを用いて，dx/dtの成分を計算
U = A[0, 0]*X + A[0, 1]*Y
V = A[1, 0]*X + A[1, 1]*Y

t = np.arange(-1.5, 1.5, 0.01)

##描画
fig, ax = plt.subplots()

#行列Aが実固有値を持つ場合のみ不変集合をプロット
if eig.imag[0] == 0 and eig.imag[1] == 0:
    ax.plot(t, (vec[1, 0]/vec[0,0])*t, ls='--')
    ax.plot(t, (vec[1, 1]/vec[0,1])*t, ls='--')

#xの位相図面をプロット
ax.streamplot(X, Y, U, V, density=0.7, color='black')
plot_set(ax, '$x_1$', '$x_2$')
ax.set_ylim(-1.5, 1.5)
ax.set_title("Phase Drawing for state 'x'")

plt.show()
