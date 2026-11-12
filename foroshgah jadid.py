def hesab_faktor (sabad,ghymat):
    jam = 0
    for kala in sabad:
        jam = jam + ghymat[kala]
    return jam
def hazf_sabad (a):
    hazf = input("chio hazf konam : ")
    if hazf in sabad:
        sabad.remove(hazf)
        print("hazf shod")
    else:
        print("kala vojod nadarad")
    

ghymat = {"sib":100, "moz":150, "anar":210}
sabad = []

print("""
-------meno foroshgah------
sib / moz / anar = kharid
tedad = didan sabad
hazf = delet
q = exit
""")

while True:

    kharid = input("sabad shoma : ")
    if kharid == "tedad":
        if len(sabad) == 0 :
            print("sabad khalie")
        else:
            print("---sabad shoma---")
            print(hesab_faktor(sabad,ghymat))
    elif kharid == "hazf":
        print(hazf_sabad(kharid))
    elif kharid == "q" :
            print("bay")
            break
    elif kharid in ghymat:
        sabad.append(kharid)
    else:
        print("nadarm")