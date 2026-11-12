print("پروژه فروشگاه")
print("گلمحمدي فروشگاه به آمديد خوش")
print("کنيد اضافه  خود سبد به را خريد اجناس لطفا  خود را به سبد خريد   ")
print(" اجناس مشاهده جهت (tedad )کنيد وارد را")
print("ببنديد را سبد  (q) انتخواب با")
print("کنيد حذف سبد از (hazf) کردن وارد با")
sabad = []
while True:
    vorodi = input(" شما سبد :  ")
    if vorodi.isdigit():
        print("کنيد وارد عدد")
        continue
    elif vorodi == "q":
        print("خداحافظ")
        break
    elif vorodi == "tedad" :
        print(f"ميباشد {len(sabad)} الان تا شما سبد")
        for kala in sabad:
            print(kala)
        continue
    elif vorodi == "hazf":
        hazf = input("کنم حذف چيو : ")
        if hazf in sabad:
            sabad.remove(hazf)
            print(f"{hazf} شد حذف شما سيد از")
        else:
            print("کنيد انتخواب خود خريدهاي از")
        continue
    sabad.append(vorodi)
    print(f"{vorodi} ezafe shod!")
