import time 

guests_list=['Maria','Kangkang','June',]
print('My dear friends:'+guests_list[0]+' and '+guests_list[1]+' and '+guests_list[2]+',l am happy to invite you to come to my party.')
time.sleep(3)
print('Because '+guests_list[2]+" have no time,so it's a pity that she can't attend our party.")
guests_list[2]='Michael'
print("now,our members are:"+str(guests_list))
time.sleep(3)

guests_list.insert(0,'Heidi')
guests_list.insert(2,'Mary')
guests_list.insert(5,'John')
print('Hello,my friends.I have a good nuws to tell you.We canhave a bigger table to hold our paty.So I decide to invite more three friends to join us.')
print('Now,my dear friends:'+str(guests_list)+',l am happy to invite you to come to my party.')

print("I'm sorry,because our nuw table can't arrive on time,so I can just invite two friends")
friend1=guests_list.pop(1)
print("I'm sorry that "+friend1+" can't attend the party.")
time.sleep(1)
friend2=guests_list.pop(1)
print("I'm sorry that "+friend2+" can't attend the party.")
time.sleep(1)
friend3=guests_list.pop(1)
print("I'm sorry that "+friend3+" can't attend the party.")
time.sleep(1)
friend4=guests_list.pop(1)
print("I'm sorry that "+friend4+" can't attend the party.")
time.sleep(2)

print("It's happy that "+guests_list[0]+" are still be invited.")
print("It's happy that "+guests_list[1]+" are still be invited.")

del guests_list[0]
del guests_list[0]
print(guests_list)
