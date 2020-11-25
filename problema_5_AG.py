n=str(input('CNP persoanei este '))
i=0
if len(n)==13:
    while ord(n) in range (48 , 58):
        i+=1
    print('CNP este corect')
else:
    print('CNP nu este corect')