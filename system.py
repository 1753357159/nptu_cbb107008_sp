import sys
ec=0;
cc=0;
xc=0;
C={'1','2','3','4','5','6','7','8','9','0'};
X={'~','!','#','%','^','&','*','=','+','?','>','<','/',',','.',':','[',']'}
E={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','R','S','T','W','V','X','Y','Z',};
a= sys.argv[1];
h= len(a);
if(h>=8 and h<=16):
    for x in range(h):
        for y in E:
            if(a[x]==y):
                ec+=1;
        for y in C:
            if(a[x]==y):
                cc+=1;
        for y in X:
            if(a[x]==y):
                xc+=1;
    if(ec!=0 and cc!=0 and xc!=0):
        print('success');
    else:
        print('fail');
else:
    print('fail');
