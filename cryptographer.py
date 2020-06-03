# Version 1.1.0
asd = "000"
st = "000"
two = "2"
lan = input("Choose your language (English, Russian):")
if lan == "English":
    print("This program encrypts one letter in English into binary")
    print("To end encryption write command end")
    print("At the beginning of the cipher is added 000 and at the end")
    print("After each encrypted letter is the number 2")
    while 2 == 2:
        a = input("What is the letter:")
        if a == "a":
            aa = "1"
            st = st + aa + two
        elif a == "b":
            bb = "10"
            st = st + bb + two
        elif a == "c":
            cc = "11"
            st = st + cc + two
        elif a == "d":
            dd = "100"
            st = st + dd + two
        elif a == "e":
            ee = "101"
            st = st + ee + two
        elif a == "f":
            ff = "110"
            st = st + ff + two
        elif a == "g":
            gg = "111"
            st = st + gg + two
        elif a == "h":
            hh = "1000"
            st = st + hh + two
        elif a == "i":
            ii = "1001"
            st = st + ii + two
        elif a == "j":
            jj = "1010"
            st = st + jj + two
        elif a == "k":
            kk = "1011"
            st = st + kk + two
        elif a == "l":
            ll = "1100"
            st = st + ll + two
        elif a == "m":
            mm = "1101"
            st = st + mm + two
        elif a == "n":
            nn = "1110"
            st = st + nn + two
        elif a == "o":
            oo = "1111"
            st = st + oo + two
        elif a == "p":
            pp = "10000"
            st = st + pp + two
        elif a == "q":
            qq = "10001"
            st = st + qq + two
        elif a == "r":
            rr = "10010"
            st = st + rr + two
        elif a == "s":
            ss = "10011"
            st = st + ss + two
        elif a == "t":
            tt = "10100"
            st = st + tt + two
        elif a == "u":
            uu = "10101"
            st = st + uu + two
        elif a == "v":
            vv = "10110"
            st = st + vv + two
        elif a == "w":
            ww = "10111"
            st = st + ww + two
        elif a == "x":
            xx = "11000"
            st = st + xx + two
        elif a == "y":
            yy = "11001"
            st = st + yy + two
        elif a == "z":
            zz = "11010"
            st = st + zz + two
        elif a == "end":
            break
elif lan == "Russian":
    print("Эта программа шифрует по ОДНОЙ букве на РУССКОМ языке в двоичный код")
    print("Чтобы закончить шифрование напишите комманду end")
    print("В начале шифра добовляется 000 и в конце")
    print("После каждой зашефрованой буквы идёт цифра 2")
    while 2 == 2:
        a = input("Назовите букву:")
        if a == "а":
            aaa = "1"
            st = st + aa + two
        elif a == "б":
            bbb = "10"
            st = st + bbb + two
        elif a == "в":
            vvv = "11"
            st = st + vvv + two
        elif a == "г":
            ggg = "100"
            st = st + ggg + two
        elif a == "д":
            dd = "101"
            st = st + ddd + two
        elif a == "е":
            ye = "110"
            st = st + ye + two
        elif a == "ё":
            yo = "111"
            st = st + yo + two
        elif a == "ж":
            zhe = "1000"
            st = st + zhe + two
        elif a == "з":
            ze = "1001"
            st = st + ze + two
        elif a == "и":
            iii = "1010"
            st = st + iii + two
        elif a == "й":
            ikr = "1011"
            st = st + ikr + two
        elif a == "к":
            ka = "1100"
            st = st + ka + two
        elif a == "л":
            lll = "1101"
            st = st + lll + two
        elif a == "м":
            em = "1110"
            st = st + em + two
        elif a == "н":
            en = "1111"
            st = st + en + two
        elif a == "о":
            ooo = "10000"
            st = st + ooo + two
        elif a == "п":
            pe = "10001"
            st = st + pe + two
        elif a == "р":
            re = "10010"
            st = st + re + two
        elif a == "с":
            sss = "10011"
            st = st + sss + two
        elif a == "т":
            ttt = "10100"
            st = st + ttt + two
        elif a == "у":
            uuu = "10101"
            st = st + uuu + two
        elif a == "ф":
            fff = "10110"
            st = st + fff + two  
        elif a == "х":
            hhh = "10111"
            st = st + hhh + two   
        elif a == "ц":
            zshe = "11000"
            st = st + zshe + two
        elif a == "ч":
            che = "11001"
            st = st + che + two
        elif a == "ш":
            sh = "11010"
            st = st + sh + two
        elif a == "щ":
            sha = "11011"
            st = st + sha + two
        elif a == "ъ":
            tverd = "11100" 
            st = st + tverd + two
        elif a == "ы":
            qwerty = "11101"
            st = st + qwerty + two
        elif a == "ь":
            mye = "11110"
            st = st + mye + two
        elif a == "э":
            eee = "11111"
            st = st + eee + two
        elif a == "ю":
            yu = "100000"
            st = st + yu + two
        elif a == "я":
            ya = "100001"
            st = st + ya + two
        elif a == "end":
            break
print(st + asd)
input("exit")
