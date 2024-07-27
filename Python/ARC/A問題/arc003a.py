y,m,d = map(int,input().split("/"))
flg = True
month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
while flg:
    ans = (y/m)%d
    if ans == 0:
        flg = False
    else:
        if y%4!=0 or (y%100==0 and y%400!=0):
            if month[m] == d:
                if m==12:
                    y,m,d = y+1,1,1
                else:
                    m,d = m+1,1

            else:
                d += 1

        else:
            if (m!=2 and month[m]) == d or (m==2 and d==29):
                if m==12:
                    y,m,d = y+1,1,1
                else:
                    m,d = m+1,1
            else:
                d+=1
print(f"{y}/{m:02}/{d:02}")

