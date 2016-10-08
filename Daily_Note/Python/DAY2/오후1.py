
# coding: utf-8

# In[ ]:


# 1. list => 입력받은 숫자들의 합!
# [1, 2, 3, 4, 5] => 15


# In[ ]:

# 2. list => 입력받은 수 중에서 가장 큰 수!
# [1, -1, 2, 105, 3, 4] => 105


# In[ ]:

def get_sum(elements):
    # sum default = 0 ---------------------
    result = 0
    # -------------------------------------
    for element in elements:
        result += element
    return result


# In[ ]:

def get_max(elements):
    result = elements[0]   # 초기값!
    for element in elements:
        if element > result:
            result = element
    return result


# In[ ]:

# 1, 2, 3, 4, 5   ( SUM )
#    3  3  4  5
#       6  4  5
#          10 5
#             15
   


# In[ ]:

# Functional Programming ( 함수형 프로그래밍 )
# Lambda
# Lambda Operator - map, filter, reduce


# In[ ]:

# map - elements 에 대해서 동일한 fn 


# In[ ]:

# n 개의 짝수 리스트 를 만드는 함수
# n=100 : 0, 2, ... , 198


# [0, ... ,99] x 2 = [0, 2, ]


# In[ ]:

def double(x):
    return x * 2

list(map(double, range(100)))


# ["", "", "fast", "", "" ]    3 의 배수일때 "fast" ( n = 100 )
def get_fast(x):
    return "fast" if (x+1)%3 == 0 else ""

list(map(get_fast, range(100)))

# ----------------------------------------------------------


list(map(lambda x: x * 2, range(100)))

list(map(
    lambda x: "fast" if (x+1)%3 == 0 else "",
    range(100),
))


# In[ ]:

# List Comprehensio
[1, 2, 3]


# In[ ]:

[i*2 for i in range(5)]  # == MAP


# In[ ]:

list(map(
    lambda x: "fast" if (x+1)%3 == 0 else "",
    range(100),
))


[
    "fast" if (i+1)%3 == 0 else ""
    for i
    in range(100)
]



# MAP - elements ... fn apply!
# FILTER - elements filtering!
# REDUCE

# 빅데이터를 처리하기 위한 기술 ... _______ MapReduce 
# ___ _____ ___ ____ => _______ _______ _________ => __________


# In[ ]:

# MAP 
# 리스트를 받아서, 양수만 뽑아서 리스트로 반환해라.

def get_positive(elements):
    result = []
    for element in elements:
        if element > 0:
            result.append(element)
    return result


# In[ ]:

list(filter(
    lambda x: x > 0,
    [-1, -2, 1, 2, 3, -4],
))


# In[ ]:

[
    i
    for i 
    in [-1, -2, 1, 2, 3, -4]
    if i > 0
]


# In[ ]:

# range(1, 10 + 1) 제곱 [1, 4, ..., 100] 중에서, 50 보다 큰 수 만 리스트 

# 1. for
# 2. lambda operator
# 3. list comprehension


# In[ ]:

result = []
for i in range(1, 10 + 1):
    if i**2 > 50:
        result.append(i**2)


# In[ ]:

list(map(
    lambda x: x**2,
    range(1, 10 + 1)
))


# In[ ]:

list(filter(
    lambda x: x > 50,
    list(map(
        lambda x: x**2,
        range(1, 10 + 1)
    )),
))


# In[ ]:

[
    i ** 2
    for i
    in range(1, 10 + 1)
]   # MAP


# In[ ]:

[
    i
    for i
    in [
        i ** 2
        for i
        in range(1, 10 + 1)
    ]
    if i > 50
]   # FILTER


# In[ ]:

[
    i ** 2
    for i
    in range(1, 10 + 1)
    if i ** 2 > 50
]


# In[ ]:

# Reduce


# In[13]:

from functools import reduce


# In[ ]:

# get_max
# get_sum


# In[ ]:

# 1 2 3 4
#   3 3 4
#     6 4
#       10


# In[14]:

def add(a, b):
    print(a, b)
    return a + b


# In[15]:

reduce(add, [1, 2, 3, 4, 5])


# In[19]:

reduce(
    lambda x, y: x + y,
    range(1, 10 + 1),
)


# In[ ]:

# get_max


# In[ ]:

# 1 0 2 -3 5 1
#   1
#     2
#        2
#          5
#              5


# In[ ]:

reduce(
    lambda x, y: x if x > y else y,
    [1, 0, 2, -3, 5, 1],
)


# In[ ]:

# 월세, 보증금


# In[40]:

rooms = [
    {"rent": 50, "deposit": 1000},
    {"rent": 55, "deposit": 2000},
    {"rent": 60, "deposit": 6000},
]


print(reduce(lambda x, y: {'rent':x['rent'] + y['rent']}, rooms)['rent'] / len(rooms))
                     

# 월세 55만원, 보증금 3000만원


# In[ ]:

# 1. for

rent_sum = 0
deposit_sum = 0

for room in rooms:
    rent_sum += room["rent"]
    deposit_sum += room["deposit"]


# In[ ]:

rent_sum / len(rooms)


# In[ ]:

deposit_sum / len(rooms)


# In[ ]:

reduce(
    lambda x,y: {"rent": x["rent"] + y["rent"]},
    rooms,
)


# In[ ]:

# {rent: 50, deposit: 1000}, {rent: 55, deposit: 2000}
# 105                                                   {rent: 60, deposit: 6000}
# 105["rent"]


# In[ ]:

reduce(
    lambda x,y: {"rent": x["rent"] + y["rent"], "deposit": x["deposit"] + y["deposit"]},
    rooms,
)


# In[ ]:




# In[ ]:




# In[ ]:

# 1. Loops
# 2. Lambda Operator - MAP, FILTER             |              REDUCE
# 3. List Comprehension


# In[ ]:




# In[ ]:

reduce(
    lambda x, y: x + y,
    [
        room["rent"]
        for room
        in rooms
    ]
) / len(rooms)


# In[ ]:




# In[ ]:




# In[ ]:

# arg, kwargs


# In[22]:

def hello(*args):     # 함수를 정의하는 시점 :: pack!
    print(args)


# In[23]:

data = (
    {"name": "dog", "weight": 5},
    {"name": "cat", "weight": 4},
    {"name": "monkey", "weight": 16},
)


# In[24]:

hello(data)


# In[25]:

hello(*data)             # 함수를 호출하는 시점 :: unpack!


# In[26]:

hello("dog", "cat", "monkey")


# In[ ]:




# In[27]:

def hello(*args, **kwargs):
    print(args)
    print(kwargs)


# In[28]:

hello()


# In[29]:

hello(1, 2, 3)


# In[30]:

hello(1, 2, 3, name="dobestan", email="dobestan@gmail.com")


# In[31]:

def get_awesome_list(n, *args):
    result = []
    
    for i in range(n):
        element = ""
        for rule in args:
            div, text = rule
            element += text if (i+1)%div == 0 else ""
        result.append(element)
        
    return result


# In[32]:

get_awesome_list(10, (2, "even"), (3, "three"))


# In[ ]:

# "" + "" + "" => ["", ""] ""
# "even" + "" + "" => ["even", ""] ""
# "" + "" + "three"
#
# 6 => "even" + "" + "three" = "eventhree"  => ["even", "three"] ""


# In[44]:

def get_awesome_list(n, *args):
return [''.join([arg[1] if (x+1)%arg[0]==0 else '' for arg in args]) for x in range(n)]
get_awesome_list(10, (2, "two"), (3, "three"))


# In[45]:

get_awesome_list(10)


# In[46]:

get_awesome_list(10, (2, "two"), (3, "three"))


# In[ ]:

# 1. get_awesome_list => List Comprehension, Lambda Operator ( map * 2)
# 2. get_sneil(n)


# In[ ]:

# n * n ( n = 3)

# [[1, 2, 3]
# [8, 9, 4]
# [7, 6 ,5]]  ( 3 x 3 )


# In[ ]:

1 2 3 4
12 13 14 5
11 16 15 6
10  9 8 7


# In[ ]:




# In[ ]:

# Python (*) --- 
# Lambda, Lambda Operator, List Comprehension 
# *args, **kwargs


# In[ ]:

# Function Advanced... -  '''''''''''''''''''
# Class...


# In[ ]:




# In[ ]:




# In[42]:

def awesome_list(n, *args):
    return [''.join([arg[1] if (x+1)%arg[0] == 0 else '' for arg in args]) for x in range(n)]


# In[43]:

print(awesome_list(100, (2, "two"), (3, "three")))


# In[ ]:

def awesome_lambda(n, *args):
    return list(map(lambda x: ''.join(map(labmda args: args[1] if (x+1)%arg[0] == 0 else '',args)), range(n))


# In[ ]:

print(awesome_lambda(100, (2, "two"), (3, "three")))


# In[33]:

k = [1,2,3,4,5,6,7,8,9,10]
k = list(map(lambda x: x * 2, k))
k


# In[34]:

k = [1,2,3,4,5,6,7,8,9,10,]
k_map = list(map(lambda x : x%2 == 0, k))
k_filter = list(filter(lambda= x: x%2 == 0, k))

print(k_map)
print(k_filter)


# In[35]:

from functools import reduce
k = [1,2,3,4,5,6,7,8,9,10,]
sum_result = reduce(lambda x, y: x+y, k)

sum_result


# In[ ]:




# In[36]:

k = [1,2,3,4,5,6,7,8,9,10,]
double_k = [i *2 for i in k]

print(double_k)


# In[38]:

k = [1,2,3,4,5,6,7,8,9,10,]
new_k = [i ** 2 for i in k if i % 3== 0 or i % 2 ==0 ]
new_k


# In[39]:

print('sum([1,2,3]) is',str(sum([1,2,3])))
print('sum(1,2,3) is',str(sum(1,2,3)))



# In[ ]:

def myprint(*args, **kwargs):
	string = ''
	for i in args:
		string += str(i)
	for key, value in kwargs.items():
		string += str(value)
	print(string)

myprint(1,2,3,4,k ='?', l = 'ok')


# In[47]:

from functools import reduce
def myprint(*args):
	for v in args:
		print(v)

list = ['철수', '영희', '불금', '함께 보냈다.']
myprint(list)


# In[12]:

def get_awesome_list(n, *args):
	args = list(args)
	args.sort(key=lambda x: x[0])
	
	return '\n'.join([''.join([arg[1] if i%arg[0]==0 else '' for arg in args]) for i in range(1, n+1)])

	return '\n'.join(map(lambda i: ''.join(map(lambda arg: arg[1] if i%arg[0] == 0 else '' ,args))
	, range(1, n+1)))

print(get_awesome_list(100, (3, 'Fizz'), (5, 'Buzz'), (7, 'Ok!'), (9, 'Too long')))


# In[7]:

k = ((3, 'Fizz'), (5, 'Buzz'), (7, 'Ok!'), (9, 'Too long'))


# In[8]:

list(k).sort(key=lambda x: x[0])


# In[ ]:



