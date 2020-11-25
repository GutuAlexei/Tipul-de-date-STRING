n=str(input('CNP persoanei este '))
if len(n)==13:
    i=0
    while  ord(n) in range (48 , 58):
        i+=1
    print('CNP este corect')
else:
    print('CNp nu este corect')