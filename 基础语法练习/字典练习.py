import time 

friend={
    'frist_name':'john',
    'last_name':'smith',
    'age':'21',
    'city':'xiamen',
    }

print(friend['city'].title())
time.sleep(2)

friend_value=friend.get('full_name','No friend value assigned')
print(friend_value)
time.sleep(2)

print(friend['age'])
time.sleep(1)
friend['age']='18'
print(friend['age'])
time.sleep(2)

del friend['frist_name']
del friend['last_name']
print(friend)
time.sleep(2)

friend['full_name']='john smith'
friend_value=friend.get('full_name')
print(friend_value)
time.sleep(1)

print(friend)
time.sleep(1)
print('End of procedure')

