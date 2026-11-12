print("""
-------meno foroshgah------
sib / moz / anar = kharid
tedad = didan sabad
hazf = delet
q = exit
""")
def hesab_faktor(sabad,ghymat):
    jam = 0
    for kala in sabad:
        jam = jam + ghymat[kala]
    return jam
def hazf_kharid(sabad):
    vorodi = input("chio hazf konam")
    if vorodi in sabad:
        sabad.remove(vorodi)
        return f"{vorodi}  hazf shod"
    else:
        return "mojod nist"

ghymat = {"sib":250, "moz":300, "anar":400}
sabad = []
jam = 0 
while True:

    kharid = input("sabad shoma : ")
    if kharid == "q":
        jam = hesab_faktor(sabad=sabad,ghymat=ghymat)
        with open(r"C:\Users\mghol\Desktop\tamrin\faktor3.txt","w",encoding="utf-8") as f :
            f.write(f"sabad : {sabad}")
            f.write(f"jam : {jam}")
        print("goodbay")
        break
    elif kharid == "tedad":
        if len(sabad) == 0 :
            print("sabad khaliye!!!")
        else:
            print("----hesab shoma----")
            print(hesab_faktor(sabad=sabad,ghymat=ghymat))
    elif kharid == "hazf":
        print(hazf_kharid(sabad))
    elif kharid in ghymat :
        sabad.append(kharid)
