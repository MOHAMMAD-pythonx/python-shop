print("عابر بانک")
print("از بین گزینه های زیر انتخواب کنید")
print("برای واریزی گزینه z")
print("برای برداشت از حساب گزینه b")
print("برای نمایش موجودی گزینه s")
print("برای خروج گزینه q")
mojodi = 1000
while True:
    vorodi = input("لطفا گزینه مورد نظر خود را وارد کنید = ")
    if vorodi == "q" :
        print("خدانگهدار")
        break
    mablagh = int (input("لطفا مبلغ مورد نظر خود را وارد کنید"))
    if vorodi == "z" :
        mojodi = mablagh + mojodi
        print(mojodi)
    elif vorodi == "b" :
        if mablagh > mojodi :
            print("برداشت امکان پزیر نمی باشد")
        elif mablagh <= mojodi :
            mojodi = mojodi - mablagh
            print(mojodi)
    elif vorodi == "s":
        print(mojodi)