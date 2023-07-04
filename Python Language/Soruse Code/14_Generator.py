#We use Generator For Memory Efficient
#It will Run Only One Time ❗
#GEN Dont store Datad

def Generator(num):
    for i in range(1,num):
        yield i

Run=Generator(10)

for i in Run:
    print(i)

#IT is will run beacuse Gen Run only one Times
for i in Run:
    print(i)    