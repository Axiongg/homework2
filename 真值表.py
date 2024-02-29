# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def truth_table():
    # 輸出表頭
    print("P\tQ\tP and Q\tP or Q\tnot(P and Q)\tnot(P or Q)\tP then Q\tQ then P\tP if and only if Q")
    
    # 遍歷所有可能的P和Q的組合
    for p in [True, False]:
        for q in [True, False]:
            # 計算邏輯運算的結果
            p_and_q = p and q
            p_or_q = p or q
            not_p_and_q = not (p and q)
            not_p_or_q = not (p or q)
            p_then_q = not p or q
            q_then_p = not q or p
            p_iff_q = (p and q) or (not p and not q)
            
            # 輸出每一行的結果
            print(f"{p}\t{q}\t{p_and_q}\t{p_or_q}\t{not_p_and_q}\t{not_p_or_q}\t{p_then_q}\t{q_then_p}\t{p_iff_q}")

# 呼叫函數以生成真值表
truth_table()

