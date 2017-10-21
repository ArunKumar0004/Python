#Function as an argument
#python version :3 
def exploder(string,num):
    print string*num;
    
def Myfun(str,fun,n):
    exploder(str,n)
    
Myfun("guvi",exploder,5)



OUTPUT:
guviguviguviguviguvi