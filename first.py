# secret.py verson 1.0.1
print("Эта программа шифрует по ОДНОЙ букве на РУССКОМ языке в двоичный код")
print("Чтобы закончить шифрование напишите end")
print("В начале шифра добовляется 000 и в конце")
print("После каждой буквы идёт цыфра 2")
asd = "000"
st = "000"
two = "2"
while 2 == 2:
    a = input("Назовите букву:")
    if a == "а":
        aa = "1"
        st = st + aa + two
    elif a == "б":
        bb = "10"
        st = st + bb + two
    elif a == "в":
        vv = "11"
        st = st + vv + two
    elif a == "г":
        gg = "100"
        st = st + gg + two
    elif a == "д":
        dd = "101"
        st = st + dd + two
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
        ii = "1010"
        st = st + ii + two
    elif a == "й":
        ikr = "1011"
        st = st + ikr + two
    elif a == "к":
        ka = "1100"
        st = st + ka + two
    elif a == "л":
        ll = "1101"
        st = st + ll + two
    elif a == "м":
        em = "1110"
        st = st + em + two
    elif a == "н":
        en = "1111"
        st = st + en + two
    elif a == "о":
        oo = "10000"
        st = st + oo + two
    elif a == "п":
        pe = "10001"
        st = st + pe + two
    elif a == "р":
        re = "10010"
        st = st + re + two
    elif a == "с":
        ss = "10011"
        st = st + ss + two
    elif a == "т":
        tt = "10100"
        st = st + tt + two
    elif a == "у":
        uu = "10101"
        st = st + uu + two
    elif a == "ф":
        ff = "10110"
        st = st + ff + two  
    elif a == "х":
        hh = "10111"
        st = st + hh + two   
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
