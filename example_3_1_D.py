line = []
while (text := input()) != "":
    if text.endswith("@@@"):
        continue
    elif text.startswith("##"):
        line.append(text[2:])
    else:
        line.append(text)
for i in range(len(line)):
    print(line[i])