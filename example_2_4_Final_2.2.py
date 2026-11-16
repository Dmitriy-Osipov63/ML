N, M, Q, cw, sw, hw, tw, = map(int, input().split())
if M > 0 and cw > 0 and sw > 0 and hw > 0 and tw > 0:
    s_name = input()
    x = 0
    count = 0
    while x < M:
        a, b, c, d = map(int, input().split(","))
        rate = (a * cw) + (b * sw) + (c * hw) + (d * tw)
        count += rate
        x += 1
    s_rate = round(count / Q * 100)
    if s_rate > Q:
        print("Во введённых данных ошибка") 
    else:
        print(f"{s_name} {s_rate}%")
else:
    print("Во введённых данных ошибка") 