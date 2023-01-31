import random

knb=["kivi", "paber", "käärid"]
su=0
sk=0
nimi=input("Mis on sinu nimi? ")
while True:
    o=input("Kivi, käärid või paber? ")
    r=random.choice(knb)
    print(f"Sa oled valinud {o}\nArvuti on valinud {r}.")
    if o==r:
        print(f"Viik.")
    elif o.lower()=="kivi" and r=="käärid":
        print("Kivi purustab käärid. Sa võidad.")
        su+=1
    elif o.lower()=="kivi" and r=="paber":
        print("Paber mähib kivi ümber. Sa kaotad.")
        sk+=1
    elif o.lower()=="paber" and r=="kivi":
        print("Paber mähitakse ümber kivi. Sa võidad.")
        su+=1
    elif o.lower()=="paber" and r=="käärid":
        print("Käärid lõikavad paberit. Sa kaotad.")
        sk+=1
    elif o.lower()=="käärid" and r=="paber":
        print("Käärid lõikasid paberit. Sa võidad.")
        su+=1
    elif o.lower()=="käärid" and r=="kivi":
        print("Kivi purustab käärid. Sa kaotad.")
        sk+=1
    else:
        print("Sisestage ainult kivi, käärid või paber")
    print(f"Punktide arv:\n{nimi}: {su}\nArvuti: {sk}")
    e=input("Kas me mängime veel? Jah või ei? ") 
    if e.lower()=="ei": 
        break