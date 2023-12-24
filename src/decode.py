from sbib import arr
def decode():
        f = open("tntd.dd", "r")
        arr2 = f.readline().split(".")
        f.close()
        values = list(arr.values())
        keys = list(arr.keys())
        f1 = open("output.txt", "w")
        for n in arr2:
                #print(keys[values.index(int(n))], end="")
                f1.write(str(keys[values.index(int(n))]))
        f1.close()
