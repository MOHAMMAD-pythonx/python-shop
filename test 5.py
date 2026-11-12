print("سیستم معدل کلاس")

tedad = int(input("چندتا نمره داری"))
a = 0
for i in range(1,tedad+1):
    nomre = int(input(f"نمره{i}ارد کن"))
    a = a + nomre
    moadel = a / tedad
    print(f"معدل: {moadel}")
    if moadel >= 10 :
        print("قبول")
    else:
        print("مردود")