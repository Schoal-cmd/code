##
num=22
count=6
while count<23:
    if f'{num:b}'.count('1')==3:
        count+=1
    num+=1
print(num-1)
