N, M, Q, cw, sw, hw, tw, = map(int, input().split())
min_rate = Q
average_rate, summ_av_rate = 0, 0
top_1_name, top_2_name, top_3_name = "", "", ""
top_1_rate, top_2_rate, top_3_rate = 0, 0, 0

if N >= 3 and M > 0 and cw > 0 and sw > 0 and hw > 0 and tw > 0 and Q > 0:
    for stud in range(N):
        s_name = input()
        summ_rate = 0
        a, b, c, d = 0, 0, 0, 0
        for lesson in range(M):
            a, b, c, d = map(int, input().split(","))
            
            summ_rate += (a * cw) + (b * sw) + (c * hw) + (d * tw)
    
        if summ_rate > top_1_rate:
            top_3_name = top_2_name
            top_2_name = top_1_name
            top_1_name = s_name
            top_3_rate = top_2_rate
            top_2_rate = top_1_rate
            top_1_rate = summ_rate
        elif summ_rate > top_2_rate:
            top_3_name = top_2_name
            top_2_name = s_name
            top_3_rate = top_2_rate
            top_2_rate = summ_rate
        elif summ_rate > top_3_rate:
            top_3_name = s_name
            top_3_rate = summ_rate
        if summ_rate < min_rate:
            min_rate = summ_rate

        summ_av_rate += summ_rate

    if summ_rate > Q:
        print("Во введённых данных ошибка")
    else:
        top_1_rate_perc = round(top_1_rate * 100 / Q)
        top_2_rate_perc = round(top_2_rate * 100 / Q)
        top_3_rate_perc = round(top_3_rate * 100 / Q)
        min_rate_perc = round(min_rate * 100 / Q)
        average_rate_perc = round((summ_av_rate / N) * 100 / Q)

    print(top_1_rate_perc, average_rate_perc, min_rate_perc)
    print(f"{top_1_name} {top_1_rate_perc}%")
    print(f"{top_2_name} {top_2_rate_perc}%")
    print(f"{top_3_name} {top_3_rate_perc}%")
    if average_rate_perc > 50:
        print("Курс усваивается хорошо")
    else:
        print("Курс усваивается плохо")
else:
    print("В введённых данных ошибка") 