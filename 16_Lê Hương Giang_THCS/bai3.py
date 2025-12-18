n = input("Nhập chuỗi n: ")
result = ""
space = False
started = False

for i in n:
    if i != ' ':
        result += i
        space = False
        started = True
    else:
        if started and not space:
            result += ' '
            space = True

print(result)