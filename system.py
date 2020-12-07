import sys
count=0;

mx={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','R','S','T','W','V','X','Y','Z',};
a= sys.argv[1];
h= len(a);
if(h>=8 and h<=16):
    for x in range(h):
        for y in mx:
            if(a[x]==y):
                count+=1;
    if(count!=0):
        print('success');
    else:
        print('fail');
else:
    print('fail');
    