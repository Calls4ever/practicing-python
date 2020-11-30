total=0
count=1
while True:
    inp= input('type a number, type done when you are don \n')
    if  inp == 'done': break
    inp=float(inp)
    total=total+inp
    print(total/count)
    count=count+1

