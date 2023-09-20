binary=[0,0,0,1,0,1,0,1]
list=[128,64,32,16,8,4,2,1]
On=[]
sum=0

for a in range(len(binary)):
    if(binary[a]==1):
        On.insert(a,a)


for a in range(len(On)):
    sum+=list[On[a]]
    
print(sum)



#IP-Binary

# Ip=[172,16,34,3]
# list=[128,64,32,16,8,4,2,1]
# On=[]

# for b in range(len(Ip)):
#     for a in range(len(list)):
#         c=Ip[b]-list[a]
#         if c<0:
#             On.insert(a,0)
#         else:
#             On.insert(a,1)
#             Ip[b]=+c
#     print("\n",On)
#     On.clear()
