import string
dict = {}
data = ""
file=open("ip_open.txt","w+")
for i in range(0, len(string.ascii_lowercase)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i+1]
print(dict)
with open("ip_open.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of file")
            break
        else:
            data=c
        print(data)
file.close()