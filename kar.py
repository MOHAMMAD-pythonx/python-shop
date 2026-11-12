print(" برنامه مدیریت کارهای روزانه ")
tasks = []
print("\n--- منوی کارهای روزانه ---")
print("1. نمایش لیست کارها")
print("2. اضافه کردن کار جدید")
print("3. خروج")
while True:
    choice = input("لطفاً شماره گزینه مورد نظر را وارد کنید (1 یا 2 یا 3): ")
    if choice == "1":
        for i in tasks:
            print(i)
    elif choice == "2":
        vorodi = input("کار جدید را وارد کنید : ")
        tasks.append(vorodi)
    elif choice == "3":
        print ("bay")
        break