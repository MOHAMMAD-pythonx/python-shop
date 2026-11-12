print("خوش آمدید به پروژه عابر بانک")
def show (c):
    return mojodi
def variz(c):
    if c == 0 or c < 0 :
        return "لطفا مبلغ را درست واریز نمایید"
    return  c + mojodi 
def bardasht(c):
    if c > mojodi:
        return "موجودی کافی نمی باشد"
    return mojodi - c

print("لطفا کارت خود را وارد کنید و سپس از گذینه های زیر یکی را انتخواب کنید")
print("برای نمایش موجودی گزینه (s)را انتخواب کنید")
print("برای واریز به حساب گزینه (v)را انتخواب کنید")
print("برای برداشت از حساب گزینه (b) را انتخواب کنید ")
print("برای خروج گزینه (q) را انتخواب کنید")
print("لطفا پس از انتخواب گزینه واریز یا برداشت مبلغ مورد نظر را وارد کنید")

mojodi = 1000

while True:
    a = input("گزینه شما : ")
    if a=="q":
        print("خدانگهدار")
        break
    if a=="s":
        print(mojodi)
        continue
    mablag = int (input("لطفا مبلغ را وارد کنید"))
    if a=="v":
        if mablag == 0 or mablag < 0 :
            print("لطفا مبلغ را درست واریز نمایید")
        else:
            mojodi = mablag + mojodi
    elif  a=="b":
        if mablag > mojodi:
            print("موجودی کافی نمی باشد")
        else:
            mojodi = mojodi - mablag   
    else:
        print("گزینه صحیح  را انخواب کنید")
       