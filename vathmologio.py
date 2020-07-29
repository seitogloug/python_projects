def check (n,a,b):
    if (n<a or n>b):
        return True
    else:
        return False

        
print('how many students do you have')
students=input()
st_grade={}
for j in range(int(students)):
    print('give student\'s name')
    name=input()
    sum=0
    max=-1
    min=11
    grades=[]
    for i in range(10):
        print('give me your grade in lesson', i)
        vathmos=int(input())
        while (check(vathmos,0,10)):
            print(' the range of the grades must be between 0 and 10')
            vathmos=int(input())
        grades=grades+[vathmos] 
        if (vathmos>max):
            max=vathmos
        if (vathmos<min):
            min=vathmos
        sum+=vathmos
    mo=sum/10
    st_grade[name] = mo
    print(mo)  
    print(max)
    print(min)
    print(grades)
for val,keys in st_grade.items():
    print('{}={}'.format(keys,val))



