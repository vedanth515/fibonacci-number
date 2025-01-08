
# finding left nearest and right nesrest fibonacci number 

num=int(input("enter a number:-"))
a,b=0,1

while a<=num:
    c=a+b
    a,b=b,c
left, right=b-a,a
print(left,right)


res= left if num-left<num-right else right

print(res)
    