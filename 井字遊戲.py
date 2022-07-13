str1 = '1 + 2 * 3'
str2 = str1.split(' ')
print('input:  '+str1)
str3=[]   
for i in range(len(str2)):
    if (str2[i][0]=='1'):
        print('      F--N--3')
    elif(str2[i][0]=='+'):
        print('   T  *')
    elif(str2[i][0]=='2'):
        print('      T--F--N--2')
    elif(str2[i][0]=='*'):
        print('E  +')
    elif(str2[i][0]=='3'):
        print('   E--T--F--N--1')