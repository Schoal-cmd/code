
import random

number=random.randint(1,100)
print('The guessing game begins')
for num in range(5):
    print('你一共有5次机会')
    guess_num=float(input('你来猜猜我的密秘数字是多少：'))
    if guess_num < number:
        print('你猜的太小了，请重新猜猜~')
    elif guess_num > number:
        print('你猜的太大了，请重新猜猜~')
    else:
        print ('恭喜你，你猜对啦！~')
        break 
print("正确答案是"+str(number)5050)