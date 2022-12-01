a=input()
l=len(a)
a=a+"   "
i=0
c=0
num=0
while(i<l):
    if(a[i]=="I"):
        if(a[(i+1)]=="V"):
            num=num+4
            break
        elif(a[(i+1)]=="X"):
            num=num+9
            break
        elif(a[i+3]=="I"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+1
    elif(a[i]=="V"):
        if(a[i+3]=="V"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+5
    elif(a[i]=="X"):
        if(a[i+1]=="L"):
            num=num+40
            i=i+1
        elif(a[i+1]=="C"):
            num=num+90
            i=i+1
        elif(a[i+3]=="X"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+10
    elif(a[i]=="L"):
        if(a[i+3]=="L"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+50
    elif(a[i]=="C"):
        if(a[i+1]=="D"):
            num=num+400
            i=i+1
        elif(a[i+1]=="M"):
            num=num+900
            i=i+1
        elif(a[i+3]=="C"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+100
    elif(a[i]=="D"):
        if(a[i+3]=="D"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+500
    elif(a[i]=="M"):
        if(a[i+3]=="M"):
            print("INVALID INPUT")
            c=1
            break
        else:
            num=num+1000
    else:
        print("INVALID INPUT")
        c=1
        break
    i=i+1
if(c==0):
    print(num)

