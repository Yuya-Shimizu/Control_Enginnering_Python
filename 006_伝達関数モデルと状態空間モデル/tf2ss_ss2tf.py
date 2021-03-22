"""
2021/02/23
@Yuya Shimizu

状態空間モデルと伝達関数モデル
"""

from control import tf, tf2ss, ss2tf, canonical_form

#適当な伝達関数モデルを準備
numerator = [0, 1]
denominator = [1, 1, 1]
P = tf(numerator, denominator)



#伝達関数モデル　→　状態空間モデル
Pss = tf2ss(P)
print(f"<伝達関数モデル → 状態空間モデル>\n{P}\n　↓\n\n{Pss}\n")

#状態空間モデル　→　伝達関数モデル
Ptf = ss2tf(Pss)
print(f"\n<状態空間モデル → 伝達関数モデル>\n{Pss}\n　↓\n{Ptf}")



#可制御正準形への変換
Pr, T = canonical_form(Pss, form = 'reachable')
print(f"\n<可制御正準形への変換>\n{Pss}\n　↓\n\n{Pr}")

#可観測正準形への変換
Pr, T = canonical_form(Pss, form = 'observable')
print(f"\n<可観測正準形への変換>\n{Pss}\n　↓\n\n{Pr}")
