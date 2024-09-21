print("python quiz \n each questions carry one marks")
print("only enters option")
name=str(input("enter your name :"))

print("Q1. which type of language does python?\na.case sensitive\tb.low level\nc.basic \t d.linux")
a=str(input("enter your answer :"))

print("Q2. which of the following is a string?\na.name\tb.'name'\nc.'''name'''\td.#name")
b=str(input("enter your answer :"))

print('Q3. which another following is integer?\na."3"\tb.3\nfour\t#3')
c=str(input("enter your answer :"))

print("Q4.Name of this operator%?\na.modules\tb.modulu\nc.percentage\tnone of the above")
d=str(input("enter your answer :"))

print("Q5.Which one of the following is arithmetic operator?\na.%\tb.'+'\nc.\\td.'''+'''")
e=str(input("enter your answer :"))

i=0
if a=="a":
    i+=1
elif a!="a":
    i+=0
if b=="c":
    i+=1
elif b!="c":
    i+=0
if c=="b":
    i+=1
elif c!="b":
    i+=0
if d=="a":
    i+=1
elif d!="a":
    i+=0
if e=="a":
    i+=1
elif e!="a":
    i+=0
print(name,"score is :",i)

if i==5:
    print("excellent")
elif i==4:
    print("very good")
elif i<=3:
    print("ja ke padh le python")

print("[answers is 1.a;2.c;3.b;4.a;5.a]")
