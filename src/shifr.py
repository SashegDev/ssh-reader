from decode import decode;from encode import encode;from sbib import arr
from os import system
import time
system('cls')
time.sleep(5)
contrub = 'SashegDev and NoicySpektr'
#licensefile = open("LIC.pt","r")
print("Добро пожаловать в Енкодер/Декодер текста")
print("Написали его:".center(50,'_'))
print(contrub.center(50, '_'))
time.sleep(3)
system('cls')
DECODE = '1.Decode'
ENCODE = '2.Encode'
EXIT = '3.Exit'
print("Что бы вы хотели сделать?")
print(DECODE.center(50,' '))
print(ENCODE.center(50,' '))
print(EXIT.center(50,' '))
def op():
    op = int(input(">>> "))
    if op==1:
        decode()
        op()
    elif op==2:
        encode()
        op()
    elif op==3:
        exit()
    else:
        print("такого выбора нет!")
        time.sleep(2)
        system("cls")
        main()


def main():
    while True:
        try:
            op()
        except ValueError:
            print("System error №1:ValueError, может быть ты написал тип str а не тип int?".center(50,'-'))
main()
    

