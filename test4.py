print ("خوش آمدید")
def zarb (a,b):
    return a*b
def taghsim (a,b):
    if b == 0 :
        return "امکان تقسیم این عدد وجود ندارد"
    return a/b
def jam (a,b):
    return a+b
def tafrigh (a,b):
    return a-b

print("از بین گذینه های زیر یکی را انتخواب کنید")
print(" برای عملگر ضرب z")
print("برای عملگر جمع s")
print(" برای عملگر تقسیم t")
print("برای عملگر تفریق m")
print("برای خروج q")

while True :
    vorodi = input("لطفا گزینه مورد نظر خود را انتخواب کنید : ")
    if vorodi == "q" :
        print("خدانگهدار")
        break
    aval = int(input("لطفا عدد خود را وارد کنید"))
    dovom = int(input("لطفا عدد خود را وارد کنید"))
    if vorodi == "z":
        print(zarb (a=aval ,b=dovom))
    if vorodi == "s" :
        print(jam(a=aval ,b=dovom))
    if vorodi == "t":
        print(taghsim(a=aval, b=dovom))
    if vorodi == "m" :
        print(tafrigh(a=aval, b=dovom))
    