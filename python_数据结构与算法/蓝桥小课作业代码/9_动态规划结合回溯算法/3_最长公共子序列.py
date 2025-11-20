#子序列：删去若干元素后得到的序列；相对顺序一致但是不连续
#子串：相对顺序一致且连续
##应用场景：字符串相似度比对、模糊查找

###暴力穷举法：o（2**（m+n））
def lcs_length(x,y):
    m,n=len(x),len(y)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]
x=['a','b','c','b','d','a','b']
y=['b','d','c','a','b','a']
print(lcs_length(x,y))
print(lcs_length("abcbdab","bdcaba"))

def lcs_length_track(x,y):
    m,n=len(x),len(y)
    dp=[[0]*(n+1) for _ in range(m+1)]
    track=[[0]*(n+1) for _ in range(m+1)] ###1向左上，2向上，3向左
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                track[i][j]=1
            elif dp[i][j-1]>dp[i-1][j]:
                dp[i][j]=dp[i][j-1]
                track[i][j]=3
            elif dp[i][j-1]<dp[i-1][j]:
                dp[i][j]=dp[i-1][j]
                track[i][j]=2
    return dp,track
#print(lcs_length_track("abcbdab","bdcaba"))

def lcs_trackback(x,y):
    dp,track=lcs_length_track(x,y)
    #print(dp,track)
    i,j=len(x),len(y)
    result=[]
    while i>0 and j>0:
        if dp[i][j]==1:
            result.append(x[i-1])
            i-=1
            j-=1
            print(i,j)
            print(result)
        elif dp[i][j]==2:
            i-=1
            print(i,j)
        elif dp[i][j]==3:
            j-=1
            print(i,j)
    a=''.join(reversed(result))
    return a
print(lcs_trackback("abcbdab","bdcaba"))