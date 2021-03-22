"""
2021/02/21
@Yuya Shimizu

ブロック線図
"""
from control import tf, series, parallel, feedback

##例で使用する2つのシステムを生成
#numerator: 分子　denominator: 分母
num1 = [0, 1]
den1 = [1, 1]
S1 = tf(num1, den1)

num2 = [1, 1]
den2 = [1, 1, 1]
S2 = tf(num2, den2)


##直列結合
S = S1 * S2
print(f"<直列結合>\n(式より){S}")
S = series(S1, S2)
print(f"(series関数より){S}\n")


##並列結合
S = S1 + S2
print(f"<並列結合>\n(式より){S}")
S = parallel(S1, S2)
print(f"(parallel関数より){S}\n")


##フィードバック結合
S = S1 / (1+ S1*S2)
print(f"<並列結合>\n(式より){S}\n\t↓約分\n{S.minreal()}")    #Pythonではうまく約分されない　約分するには，minrealメソッドを使う
S = feedback(S1, S2)
#フィードバック部分にシステムがない場合は，第2引数を1として考える，もしくは第1引数のみで実行する．
#また，ポジティブフィードバックの場合は，第3引数目sign=1と指定する
print(f"(feedback関数より){S}\n")

