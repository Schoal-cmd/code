#1.0
print('1 X 1 = 1')
print('1 X 2 = 2  2 X 2 = 4')
print('1 X 3 = 3  2 X 3 = 6  3 X 3 = 9')
print('1 X 4 = 4  2 X 4 = 8  3 X 4 = 12  4 X 4 = 16')
print('')
#2.0
for a in range(1,10):
    for b in range(1,a+1):
        result=b*a
        print('%s x %s = %s'%(b,a,result),end='  ')
    print('')

#3.0 封装成一个函数
def math():
    for a in range(1,10):
        for b in range(1,a+1):
            result=b*a
            print('%s x %s = %s'%(b,a,result),end='  ')
        print('')
math()

#4.0
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))