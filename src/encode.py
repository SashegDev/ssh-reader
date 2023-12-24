from sbib import arr
def encode():
    f = open("tntd.dd", "w+")
    print("в шифре разрешены только буквы!".center(50,' '))
#    sd = int(input("Сдвиг шифратора: "))
    text = input("Ваш текст: ")
    values = list(arr.values())
    keys = list(arr.keys())
    for n in text:
        #print(values[keys.index(n)], end=".")
        f.write(str(values[keys.index(n)]))
        f.write(".")
    with open("tntd.dd", "ab") as f1:
        f1.truncate(f.tell() - 1)
    f.close()

