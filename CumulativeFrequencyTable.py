def CFT(a): # Cumulative Frequency Table
    c={}
    b=['10 - 20','20 - 30','30 - 40','40 - 50','50 - 60']
    for d in range(len(b)):
        c[b[d]]=0
    for d in a:
        if d < 20:
            c[b[0]]+=1
        elif d < 30:
            c[b[1]]+=1
        elif d < 40:
            c[b[2]]+=1
        elif d < 50:
            c[b[3]]+=1
        else:
            c[b[4]]+=1
    print(f"Frequency: {c}\n\nCumulative Frequency: ",end='')
    e=0
    for d in range(len(b)):
        e+=c[b[d]]
        print(e,end=' ')
    print(f"\n\nTotal Frequency = {e}\n")
    for d in range(5):
        c[b[d]]=round(c[b[d]]/len(a)*100)
    print(f"Percent: {c}\n\nCumulative Percent: ",end='')
    e=0
    for d in range(len(b)):
        e+=c[b[d]]
        print(e,end=' ')
    print(f"\n\nTotal Percent = {e}")
CFT(sorted([12,13,17,21,24,24,26,27,27,30,32,35,37,38,41,43,44,46,53,58]))