annee = int(input (f"Saisissez une année\n"))
if (annee%4 != 0):
    print ("ce n'est pas une annee bissextile")
else:
    if (annee%100 == 0 and annee%400 != 0):
        print ("ce n'est une annee bissextile")
    else :
        print ("c'est une annee bissextile")


