T=int(input())
for t in range(T):
    tt1=[]
    tt2=[]
    don=[]
    cd=0
    jd=0
    str=['C']
    final=''
    N=int(input())
    for i in range(N):
            tt1.append(list(map(int, input().split())))
    tt2=tt1.copy()
    tt1.sort()
    cd=tt1[0][1]
    for i in range(1,N):
        if tt1[i][0]>=cd or tt1[i][0]>=jd:
            if tt1[i][0]>=cd:
                str.append('C')
                cd=tt1[i][1]
            else:
                str.append('J')
                jd=tt1[i][1]
        else:
            final='IMPOSSIBLE'
    if(final != 'IMPOSSIBLE'):    
        for i in range(N):
            for j in range(N):
                if(tt2[i]==tt1[j] and j not in don):
                    final=final+str[j]
                    don.append(j)
                    break
    print("Case #{}: {}".format(t+1,final))