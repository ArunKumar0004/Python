#Fibonnaci series in list:
#python version :3 
a=0
b=1
c=0
n=10
mylist=[]
print "The fibonacci series is:"
for i in range(1,n):
    print a
    mylist.append(a)
    c=a+b
    a=b
    b=c
print "The list is:"
print mylist