#!/usr/bin/python
padding=30
from decimal import Decimal, getcontext

# getcontext().prec = 3
cols=12
l=[Decimal(float(x)/float(cols)) for x in xrange(1,cols+1)][::-1]
container = 970-padding+2
num1=cols
num2=cols
x=[".col-md-"+str(y) for y in xrange(1,13) ]
y=",".join(x)
floatleft="float:left;"
_displayinline="_display:inline;"
hack="*"
print y+"{"
print floatleft,_displayinline
print "}"
print ".container{width:%dpx\9;}" % 970
print ".container{*width:%dpx;}" % 940
for x,e in enumerate(l):
    print ".col-md-%s{" % (cols-x)
    
    print "     width:%s%%;}" % (str(float(e*100)))

for p,i in enumerate(l):
    if num1 ==1:
        continue
    if num1 is not 12:
        print ".col-md-%s{" % num1
    for t,j in enumerate(l):
        c=i*container

        r=j-padding/c
        
        if r<0:
            continue
        print "    .col-md-%s{" % num2

        print "     %swidth:%s%%;}" % (hack,str(float(r*100)))
        num2-=1
    
    if num1 is not cols:
        print "}"
    num2=cols
    num1-=1