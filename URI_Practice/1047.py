n= input().split()
starhour= int(n[0])
startmin= int(n[1])
endhour= int(n[2])
endmin= int(n[3])
if (starhour and endhour)<=24 and (startmin and endmin)<=60 and starhour>endhour and startmin>endmin:
     print("O JOGO DUROU "+ str(24-starhour-endhour)+" HORA(S) E "+str(60-startmin-endmin)+" MINUTO(S)")
elif (starhour and endhour)<=24 and (startmin and endmin)<=60 and starhour>endhour and startmin<endmin:
    print("O JOGO DUROU "+ str(24-starhour-endhour)+" HORA(S) E "+str(endmin-startmin)+" MINUTO(S)")
elif startmin==endmin and starhour==endhour:
    print("O JOGO DUROU 24 HORA(S) E 00 MINUTO(S)")
elif (starhour and endhour)<=24 and (startmin and endmin)<=60 and starhour<endhour and startmin<endmin:
    print("O JOGO DUROU " + str(endhour-starhour) + " HORA(S) E " + str(endmin - startmin) + " MINUTO(S)")
elif (starhour and endhour)<=24 and (startmin and endmin)<=60 and starhour < endhour and startmin > endmin:
    print("O JOGO DUROU " + str(endhour - starhour) + " HORA(S) E " + str(60 - startmin + endmin) + " MINUTO(S)")

#sh>eh & sm>em
#sh>eh & sm<em
#sh=eh & sm=em
#sh<eh & sm<em
#sh<eh & sm>em