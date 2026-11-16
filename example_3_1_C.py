L = int(input())
N = int(input())
text = []
for i in range(N):
    text.append(input())
for x in range(N):
    if len(text[x]) > L:
        print(text[x][:L - 3] + '...')
    else:
        print(text[x])