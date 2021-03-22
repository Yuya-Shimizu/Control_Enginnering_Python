"""
2021/02/25
@Yuya Shimizu

図を整えるための関数定義
"""

#グラフをプロットするときの線種を決めるジェネレータ
def linestyle_generator():
    linestyle = ['-', '--', '-.', ':']
    lineID = 0
    while True:
        yield linestyle[lineID]
        lineID = (lineID + 1) % len(linestyle)


#グラフを整える関数
def plot_set(fig_ax, *args):
    fig_ax.set_xlabel(args[0])   #x軸のラベルを1つ目の引数で設定
    fig_ax.set_ylabel(args[1])   #y軸のラベルを2つ目の引数で設定
    fig_ax.grid(ls=':')             #グラフの補助線を点線で設定
    if len(args) == 3:
        fig_ax.legend(loc=args[2])  #凡例の位置を3つ目の引数で設定

#ボード線図を整える関数
def bodeplot_set(fig_ax, *args):
    #ゲイン線図のグリッドとy軸ラベルの設定
    fig_ax[0].grid(which='both', ls=':')
    fig_ax[0].set_ylabel('Gain [dB]')

    #位相線図のグリッドとx軸, y軸ラベルの設定
    fig_ax[1].grid(which='both', ls=':')
    fig_ax[1].set_xlabel('$\omega$ [rad/s]')
    fig_ax[1].set_ylabel('Phase [deg]')

    #凡例の表示
    if len(args) > 0:
        fig_ax[1].legend(loc=args[0])  #引数が1つ以上：ゲイン線図に表示
    if len(args) > 1:
        fig_ax[0].legend(loc=args[1])  #引数が2つ以上：位相線図にも表示        
