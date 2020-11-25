s1=str(input('Primul cuvant este :'))
s2=str(input('Al doilea cuvant este :'))
s3=str(input('Al treilea cuvant este :'))
s4=str(input('Al patrulea cuvant este :'))
if len(s1)>=3 and len(s2)>=3 and len(s3)>=3 and len(s4)>=3:
    cuvantul=s1[0]+s1[1]+s2[0]+s3[0]+s3[1]+s3[2]
    for n in range (len(s4)//2):
        cuvantul+=s4
    print('cuvntele sunt' , s1 ,',', s2 , ',',s3 ,',', s4 , '.')
    print('Cuvantul nou este' , cuvantul , '.')
else:
    print('Nu este respectata conditia')