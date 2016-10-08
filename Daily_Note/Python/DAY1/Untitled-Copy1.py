
# coding: utf-8

# In[12]:

# 1. Shift + Enter => Execute
# 2. Esc + dd => 그 줄이 삭제 ( vi )


# In[13]:

# 자료형 ( Data Types )


# In[14]:

1 + 2  # Number


# In[15]:

100


# In[18]:

"1000"  # 문자열 ( String )
        # 내장된 기능... 


# In[20]:

"안녕하세요, " + "저는 안수찬입니다."   # concat


# In[ ]:




# In[ ]:




# In[ ]:




# In[22]:

# 여러개의 Data ...
# List, Dict, Tuple, Set ( 여러개의 데이터, Loops )


# In[23]:

# List
# 여러 데이터 ; 순서 O; 중복 O


# In[36]:

animals = [
    "dog",  # 0
    "cat",  # 1
    "fish",  # 2
    "monkey",
    "dog",
    "dog",
]


# In[41]:

animals[0]

# 0, 1, 2, 3, ,...., n-1


# In[42]:

animals[2]


# In[43]:

animals[-1]


# In[44]:

animals[-2]


# In[45]:

animals[-3]


# In[46]:

animals[0:2]


# In[48]:

animals[0:]


# In[49]:

animals[:3]


# In[53]:

animals[::2]


# In[54]:

animals[::-1]


# In[55]:

# 1 x N
# 3 x 3


# In[57]:

a = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]


# In[59]:

a[0][0]


# In[60]:

# List => Elements; Order O; Duplicate O
# Set => Elements; ( = 집합 ) ; Order X; Duplicate X


# In[61]:

animals


# In[62]:

set([1, 1, 2, 2, 3])


# In[65]:

# 우리가 가지고 있는 리스트에서
# 중복을 포함하지 않는 데이터만 다시 리스트로 만드는 작업.


# In[66]:

animals


# In[69]:

set(animals)  # 순서가 보장 X


# In[70]:

list(set(animals))   # *


# In[72]:

# List (*) - elements, order O, duplicate O
# Set - elements, order X, duplicate X


# In[73]:

# Dict (사전) - elements... O, key -> value
# Tuple


# In[74]:

animals


# In[75]:

student = {
    "name": "안수찬",
    "email": "dobestan@gmail.com",
}


# In[77]:

student


# In[78]:

student["name"]


# In[79]:

student["phonenumber"] = "Phonenumber"


# In[80]:

student


# In[81]:

# Tuple - elements O, order O, duplicate O, ( 변하지 X )


# In[82]:

(100, 200)


# In[83]:

a, b = (100, 200)


# In[84]:

a


# In[85]:

b


# In[87]:

a, b, c  = (100, 200, 300)


# In[ ]:

# List - 순서 O, 중복 O -> indexing [_____:____:_____]; 0부터 시작하는 숫자 key => value
# Set - 순서 X, 중복 X  -> `list(set(___________))`
# Dict - {Key => Value}, 순서 X, 중복 X
# Tuple - 순서 O, 중복 O, 변할 수 X


# In[88]:

# Loops


# In[94]:

for _ in range(10):
    # print("hello world")
    pass


# In[95]:

animals


# In[101]:

for animal in animals:
    print(animal)


# In[102]:

for i in range(len(animals)):
    animal = animals[i]
    print(animal)


# In[103]:

# Dict Loops


# In[104]:

student


# In[105]:

# name => 안수찬
# email => dobestan@gmail.com
# phonenumber => Phonenumber
# (순서는 바뀔 수 있습니다.; Dict => 순서 보장 X)


# In[107]:

for key in student:
    value = student[key]
    print(key + " => " + value)


# In[109]:

for something in student.items():
    key, value = something
    print(key + " => " + value)


# In[111]:

for key, value in student.items():
    print(key + " => " + value)


# In[4]:

students = [
    ["안수찬", "dobestan@gmail.com", "010-2220-5736"],
    ["안수찬2", "dobestan2@gmail.com", "010-2220-5736"],
    ["안수찬3", "dobestan3@gmail.com", "010-2220-5736"],

]


# In[119]:

# {
#     "1": {
#         "Name": "안수찬",
#         "Email": "dobestan@gmail.com",
#         "phonenumber": "010-2220-5736",
#     },
#     "2": {...}
# }


# In[5]:

data = {}


for i in range(len(students)):
    student = students[i]
    
    student_data = {}

    student_data["Name"] = student[0]
    student_data["Email"] = student[1]
    student_data["Phonenumber"] = student[2]
    
    data[str(i + 1)] = student_data
    
    print(student_data)


# In[6]:

data

# Dict of Dict
# List of Dict ... *


# In[ ]:




# In[139]:

# 조건문 ( Conditional Statement )


# In[140]:

# 양수, 음수, 0 체크하는 코드


# In[141]:

my_num = 20


# In[145]:

if my_num > 0:
    print("양수입니다.")
    
if my_num < 0:
    print("음수입니다.")
    
if my_num == 0:
    print("0 입니다.")


# In[149]:

my_num = 0
if my_num > 0:
    print("양수입니다.")
else:
    if my_num < 0:
        print("음수입니다.")
    else:
        print("0 입니다.")


# In[150]:

if my_num > 0:
    print("양수입니다.")
elif my_num < 0:
    print("음수입니다.")
else:
    print("0입니다.")
    
# if, elif, elif, elif, else


# In[151]:

my_num > 0


# In[152]:

True


# In[153]:

False


# In[160]:

# 개발 환경... (*) -> python 3.5
# pyenv, virtualenv, autoenv...
# virtualbox ubuntu + mac


# In[ ]:

# pyenv => 언어 버전
# virtualenv => 프로젝트 버전 ( 라이브러리 )
# -------
# autoenv -> activate 자동화 ( profile per dir ; ~/.bash_profile ) 


# In[ ]:

# Screen Multiplexer - Screen, Tmux 
# Editor - VIM


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[1]:

k = [1,2,3,4,5]
for i in k:
  print(i)


# In[ ]:



