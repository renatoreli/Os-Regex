import re
text = '''
    asdfhjlkjhkjhkjhkjhfasdfa
    ASDFKJSLAKDFJALSKDFJALSKDFJ
    1435468545

    JKhkjKJHKJhjk
    lkj LKFSDJALKlkj KJLKJsaf sadf 6544


    Meta characteri: . ^ $ * + ? { } [ ] \ | ( )

    a00bb00bb
    dariokarl.sl@gmail.com

    034-561-0564
    034/556 1231
    +385911234567

    www.aicentarlipik.com

    Pero Perić

    gđa. Ruslan

    Kljukica Kvakić kvakvakva

    g. Hrvoje Hrvač

'''
velika_slova=re.findall(r'[A-Z]+',text)
if len(velika_slova)>0:
    print(velika_slova)