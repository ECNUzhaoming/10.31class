
# coding: utf-8

# In[1]:

def print_numbers(n):
    print(n,end=" ")
    if n>1:
        print_numbers(n-1)
print_numbers(5)


# In[1]:

def Fib(i):
    if i==1 or i==0:
        return 1
    else:
        return Fib(i-1)+Fib(i-2)
    
print(Fib(36))


# In[2]:

cache=dict()
def fib_cache(i):
    global cache
    if i in (0,1):
        return 1
    else:
        result=cache.get(i)
        if result is None:
            result=fib_cached(i-1)+fib_cached(i-2)
            cached[i]=result
            return result


# In[4]:

fib_cache(100)


# In[9]:

from functools import lru_cache

@lru_cache(maxsize=None)
def Fib(i):
    if i==1 or i==0:
        return 1
    else
        return Fib(i-1)+Fib(i-1)

Fib(1000)


# In[19]:

def hanoi(n,source,target,temp):
    if n==1:
        print("{}->{}".format(source,target))
    else:
        hanoi(n-1,source,temp,target)
        print("{}->{}".format(source,target))
        hanoi(n-1,temp,target,source)
        
hanoi(3,"A","C","B")


# In[21]:

#生成器generator
for i in range(0,10):
    print(i,end=" ")

print("***")
a=list(range(0,10))#会在内存提前分配空间
for item in a :
    print(item,end=" ")

r=range(0,10)
# In[24]:

def fib(n):
    result=[0,1]
    second_last=0
    last=1
    for i in range(n-2):
        second_last,last=last,second_last+last
        result.append(last)
        
    return result

print(fib(5))


# In[28]:

def fib_gen(n):
    second_last=0
    last=1
    yield 0
    yield 1
    for i in range(n-2):
        second_last,last=last,second_last+last
        yield last

        

for i in fib_gen(10):
    print(i,end=" ")


# In[36]:

nested=[[1,2],[3,4],[5]]
#[1,2,3,4,5]

def flatten(nested):
    result=list()
    for sublist in nested:
        for item in sublist:
            result.append(item)
    return result
flatten_list=flatten(nested)
print(flatten_list)


# In[35]:

nested=[[1,2],[3,4],[5],6]
#[1,2,3,4,5]

def flatten(nested):
    result=list()
    for sublist in nested:
        try:
            for item in sublist:
                result.append(item)
        except TypeError:
            result.append(sublist)

    return result
flatten_list=flatten(nested)
print(flatten_list)


# In[38]:

nested=[[1,2],[3,4],[5],6]
#使用生成器节约内存，避免中间数据的产生
def flatten(nested):

    for sublist in nested:
        try:
            for item in sublist:
                yield item
        except TypeError:
            yield sublist

for item in flatten_list:
    print(item,end=" ")


# In[44]:

nested=[[1,[2,3,4]],[3,4],[5],6]
def flatten(nested):
    result=list()
    for sublist in nested:
        try:
            for item in flatten(sublist):
                result.append(item)
        except TypeError:
            result.append(sublist)

    return result
flatten_list=flatten(nested)
print(flatten_list)


# In[45]:

nested=["hello",[1,[2,3,4]],[3,4],[5],6]
def flatten(nested):
    result=list()
    for sublist in nested:
        try:
            for item in flatten(sublist):
                result.append(item)
        except TypeError:
            result.append(sublist)

    return result
flatten_list=flatten(nested)
print(flatten_list)


# In[51]:

nested=["hello",[1,[2,3,4]],[3,4],[5],6]
def flatten(nested):
    try:
        try:nested+""
        except TypeError:pass
        else:raise TypeError
            
        for sublist in nested:
            try:
                for item in flatten_list:
                    yield item
            except TypeError:
                yield sublist
                
    except TypeError:
        yield nested
    

for item in flatten(nested):
    print(item,end=" ")


# In[53]:

def func(x):
    return x.isalnum()

seq=["Hello","41","x3","**"]
list(filter(func,seq))


# In[54]:

"!".isalnum()


# In[55]:

list(filter(lambda x:x.isalnum(),seq))


# In[56]:

[x for x in seq if x.isalnum()]


# In[57]:

list(map(str,range(10)))


# In[58]:

[str(i) for i in range(10)]


# In[61]:

from functools import reduce
numbers=[1,2,4,5,6]
reduce(lambda x,y:x+y,numbers)


# In[69]:

from time import sleep
def init_bar(bar,length=80):
    bar=list()
    for i in range(length):
        bar.append(" ")
    return bar

def clear_bar(bar):
    for i in range(len(bar)):
        bar[i]=" "
        
def init_ants(bar_length=80):
    ants=list()
    ants.append({"position":0,"direction":1})
    ants.append({"position":bar_length-1,"direction":-1})
    return ants

def update_bar(bar,ants):
    clear_bar(bar)
    for ant in ants:
        if 0<=ant["position"]<len(bar):
            bar[ant["position"]]="*"
  

def is_bar_empty:
    for item in bar:
        if
    
def show_bar(bar):
    for ch in bar:
        print(ch,sep=" ",end=" ")
    print("".end="\r")
    
def update_ants(ants)：
    for ant in ants:
        ant["position"]+=ants["direction"]
        
bar=init_bar(80)
ants=init_ants()

update_bar(bar,ants)
while not is_bar_empty(bar):
    sleep(0.5)
    update_ants(ants)
    update_bar(bar,ants)
    show_bar(bar)


# In[ ]:




# In[ ]:



