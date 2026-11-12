#ghymat = {"sib":150, "moz":2000,  "anar":520  }
#print(ghymat["moz"])
#ghymat["moz"] = 32500
#print(ghymat["moz"])
#print(len(ghymat))
#if "khyar" in ghymat:
#    print(ghymat["khyar"])
#else:
#    print("vojod nadarad")#

#for mive, gemat in ghymat.items():
#    print(f" {mive} --> {gemat} toman")

#sabad = {"sib":100, "moz":200}

#print(sabad["moz"])
#if "anar" in sabad:
#    print(sabad["anar"])
#else:
#    print("nadarim")
#sabad ["anar"] =100
#rint (sabad)
#ghymat = {"sib":150, "moz":2000,  "anar":520  }
#sabad = []
#jam = 0
#print(ghymat)
#print("baray jam faktor jam ra vared konid , baray khoroj (q) ra vared konid")

#while True:
 #   a = input("Entery : ")
 #   
 #   if a == "q":
 #       print("bay")
 #       break
#    if a == "jam":
#        for kala in sabad:
#            jam = jam + ghymat[kala]
#    print(f"gam faktor : {jam}")
        
#sabad.append(a)


# gheymat = {"sib": 100, "moz": 200, "anar": 100}
# sabad = ["sib", "moz", "sib"]
# jam = 0
# for kala in sabad:
#     jam = jam + gheymat[kala]
# print(f"جمع فاکتور: {jam}") 


gheymat = {"sib": 100, "moz": 200, "anar": 150}
print("""
-------meno foroshgah------
sib / moz / anar = kharid
tedad = didan sabad
hazf = delet
q = exit
""")

sabad = []

jam = 0

while True:

    kharid = input("sabad : ").lower()

    if kharid == "tedad":
        if len(sabad) == 0:
            print("sabad khalie")
        else:
            print("----list shoma----")
            jam = 0
            for kala in sabad:
                print(f"---{kala}---")
                jam = jam + gheymat[kala]
            print(f"Jam-e faktor: {jam}")
        continue
    elif kharid == "hazf":
        hazf = input("chio hazf konam : ")
        if hazf in sabad:
            sabad.remove(hazf)
            print("hazf shod")
        else:
            print("kala vojod nadarad")
        continue
    elif kharid == "q" :
        print("bay")
        break
    elif kharid in gheymat:
        sabad.append(kharid)
    else:
        print("nadarm")


sabad.append(kharid)
