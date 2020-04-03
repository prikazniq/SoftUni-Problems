dohod = float(input())
uspeh = float(input())
zaplata = float(input())


if zaplata <= dohod or uspeh < 4.5:
    print("You cannot get a scholarship!")
if dohod <= zaplata and uspeh >= 4.5:
    print("You get a Social scholarship {0} BGN".format(round((zaplata - (zaplata * 0.65)))))
elif 6 >= uspeh > 5.50:
    print("You get a scholarship for excellent results {0} BGN".format(round(uspeh*25, 2)))
