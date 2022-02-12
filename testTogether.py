def addf():
    a = int(input("請輸入被加數:"))
    b = int(input("請輸入加數:"))
    c = "這是您的和:", a + b
    c = ''.join(str(i) for i in c)
    print(c)
    return c
addf()
