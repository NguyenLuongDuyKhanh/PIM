#Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?

dau=35
chan=94

for tho in range(dau+1):
        ga=dau-tho
        if 2*tho+4*ga==chan:
            #So Tho và So Ga
            print(tho,ga)
            break
