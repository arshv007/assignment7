#Q1ues1
d={}
n=int(input("Enter no. of items: "))
for x in range(n):
    a=input("Enter key ")
    b=input("Enter value ")
    d[a]=b
print(d)
val=input("Enter value to find:")
for y,z in d.items():
    if(z==val):
        print("Key of value",val,"is",y)

#Ques2
x={}
n=int(input("Enter number of items: "))
for i in range(n):
    name=input("Enter name ")
    y={}
    m1=int(input("Enter marks-DS: "))
    m2=int(input("Enter marks-DBMS: "))
    m3=int(input("Enter marks- PYTHON :"))
    y['DS']=m1
    y['PYTHON']=m2
    y['DBMS']=m3
    x[name]=y
print(x)
z=input("Enter name of student :")
print(x[z])
