def task_1():
    list=[1,2,3,4,5]
    print(list[0])
    print(list[2])
    print(list[0:3])
#task_1()

def task_2():
    list=["Ростов","+","на","-","Дону"]
    list[1]="-"
    print(list[0]+list[1]+list[2]+list[3]+list[4])
#task_2()

"""def task_3_1():
       list=["a","s","1","a","32","23"]
        list.sort()
        list1=list[0:3]
        list2=list[3:]
        print(list1,list2)
task_3_1()"""

def task_3_2():
    list=["a","s","1","a","32","23"]
    list1=list[0:2]
    list1.append(list[3])
    list2=[]
    list2.append(list[2])
    list2.extend(list[4:])
    print(list1,list2)
#task_3_2()

def task_4():
    list=["a","s","a"]
    list.pop()
    list.reverse()
    print(list)
#task_4()

def task_5():
    list=["a","s","1","a","32","23"]
    set1=set(list)
    print(list)
    print(set1)
#task_5()