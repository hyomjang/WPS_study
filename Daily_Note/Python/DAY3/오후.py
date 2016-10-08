
# coding: utf-8

# In[126]:

# List, Dict
# histogram


# input: ["fast", "campus", "fast", "campus", "school", "fast", "fast"]
# "fast" => 4, "campus" => 2, "school" => 1


# In[127]:

# fast           ====
# campus         ==
# school         =

"fast     ====\ncampus     ==\nschool     ="

# print!


# In[6]:

def histogram(elements):
    # 0. hist 초기화
    hist = {}
    for key in elements:
        hist[key] = 0
        
    # 1. hist 데이터 생성
    for key in elements:
        hist[key] += 1
        
    # 2. 출력
    for key, value in hist.items():
         print("{key}{space}{histogram}".format(
             key=key,
             space=" " * (10-len(key)),
             histogram="="*value,
         ))
    result = "\n".join([
        "{key}{space}{histogram}".format(
            key=key,
            space=" " * (10-len(key)),
            histogram="="*value,
        )
        for key, value
        in hist.items()
    ])
    
    return result
    
    print("\n".join(
        list(map(
            lambda key: "{key}{space}{histogram}".format(
                key=key,
                space=:" " * (10-len(key)),
                histogram="="*hist[key],
            ),
            hist, 
        ))
    ))
        
    # 1. List Comprehension
    # 2. Sort
    
    return result



# In[2]:

histogram(["fast", "campus", "fast", "campus", "school", "fast", "fast"])


# In[3]:

print(hist)


# In[ ]:




# In[84]:

# sort


# In[86]:

# fibonacci - recursive - DP memoization


# In[ ]:




# In[1]:

data = [3, 2, 1, 4, 5]


# In[ ]:

# data.sort()


# In[2]:

sorted(data)


# In[3]:

data


# In[44]:

hist


# In[11]:

# sorted(hist)


# In[136]:

data = [("python", 30), ("ruby", 20), ("javascript", 10)]


# In[137]:

sorted(data, key=lambda x: x[1])


# In[22]:

# sorted => key list


# In[1]:

sorted(hist, key=lambda key: hist[key])[::-2]


# In[ ]:




# In[ ]:




# In[27]:

# 피보나치 수열 
# 0 1 1 2 3 5 8 13 21 ...


# In[50]:

def fibo(n):
    # n번째의 피보나치 수열 숫자를 리턴하는 함수 ( for )
    
    prev, cur = 0, 1   # tuple
    if n == 0:
        return 0
    
    for i in range(n-1):    # n=2
#         temp = prev
#         prev = cur
#         cur = temp + cur    # (prev, cur) | (0, 1) => (1, 1) => (1, 2) => (2, 3) => (3, 55)
        prev, cur = cur, prev + cur
    
    return cur


# In[51]:

# 피보나치 => f(n) = f(n-1) + f(n-2)           # 재귀함수 => 함수 정의부를 포함하여 2줄 
# 팩토리얼 => f(n) = n * f(n-1)


# In[52]:

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


# In[53]:

factorial(5)


# In[ ]:




# In[60]:

def fibo_recursive(n):
#     if n == 0:
#         return n
#     if n == 1:
#         return n

#     if n < 2:
#         return n
#     return fibo_recursive(n-1) + fibo_recursive(n-2)

    return n if n < 2 else fibo_recursive(n-1) + fibo_recursive(n-2)


# In[61]:

for i in range(10):
    print(fibo_recursive(i))


# In[ ]:




# In[ ]:




# In[62]:

def fibo_recursive(n):
#     if n == 0:
#         return n
#     if n == 1:
#         return n

#     if n < 2:
#         return n
#     return fibo_recursive(n-1) + fibo_recursive(n-2)

    return n if n < 2 else fibo_recursive(n-1) + fibo_recursive(n-2)


# In[63]:

# f(5) = f(4) + f(3)
#      = (f(3) + f(2)) + (f(2) + f(1))
#      = ((f(2) + f(1))) ...

# f(n) = n...    # O(n) = n^2
# 결과값을 저장해두는 방법 ( memoization )


# In[64]:

# 동적 계획법 ( Dynamic Programming; 기억하며 풀기 )
# ___________________________ ( 큰 문제 ) => _____, _____, _____ ( 작은 문제들로 구분 )
# Memoization ( Memorization (X) ) => "Memo"


# In[65]:

# f(5) : f(5) 가 이전에 연산된적이 있나?
#        return f(5)
#        없다면, f(4) + f(3)
#           - f(4) ? return
#           - f(3) ? return


# In[68]:

# memo = []  # 피보나치 수열의 결과... 저장!  ( cache )
cache = {}


# In[6]:

__fibo_recursive_cache = {}                       # Decorator 안에서 Cache 라고 하는 {} 초기화

def fibo_recursive(n):
    if n in __fibo_recursive_cache:
        return
    else:
        result = n if n < 2 else fibo_recursive(n-1) + fibo_recursive(n-2)
        __fibo_recursive_cache[n] = result
        return result


# In[138]:

def memoize(func):
    __cache = {}
    
    def wrapper(*args):
        if args in __cache:
            return __cache[args]
        else:
#             return __cache[args] = func(*args)  # unpack
#             return __cache[args]
            __cache.update({args: func(*args)}) or __cache[args]
    
    return wrapper


# In[139]:

@memoize
def fibo(n):
    return n if n < 2 else fibo(n-1) + fibo(n-2)


# In[144]:

animals = {}


# In[149]:

animals.update({"hello": "world2"})   # None


# In[150]:

animals


# In[151]:

None or 3


# In[152]:

False or 10


# In[172]:

def memoize(func):
    __cache = {}
    return lambda *args: __cache[args] if args in __cache else __cache.update({args: func(*args)}) or __cache[args]


# In[ ]:




# In[173]:

# Python Django

# DB => user_id => user
# /posts/ => PostList ( cache ) => 
# HTML Cache


# In[174]:

# Python Django  => Full Stack Framework ( Router, Render, DB, MVC )
#                   - Router, Render, Cache, Model, ... MVC?
#                   - ? func. Class
# Python Flask   => micro framework ( Router , Request, Response ) + a
#


# In[175]:

# Matlab ...
# Ruby on Rails ( Ruby Full Stack Framework )           (*)
# Ruby Sinatra ( Ruby Micro Framework )
# Python Flask
# python Django                                         (*)
# Node.js Express ( Micro Frmamework )                   (*)


# In[176]:

# MicroFramework
# HTML, CSS, Javascript  ---- Backend? PHP, JAVA, Python,...

# Google Chrome V8 Engine
# 웹 브라우저 -> 서버 ( Javascript :: Node.js )

# 웹 클라어언트 , 웹 서버 => Javascript


# In[177]:

# 웹 브라우저 => Javascript 
# Node.js ( 서버 ) == Python 


# In[178]:

# ECMAScript 1, 2, 3, 4,5 => Class X, Function
# ECMAScript2016(ECMA6, 7) => Class.,,, +++

# Node.js (4.4) => 6.6


# In[ ]:

# Django 과거의 버전
# Django 1.10 ( = Django.1.9 ) => Django 1.4 => !.5


# In[ ]:




# In[ ]:




# In[202]:

# loops
# list comprehension
# lambda + lambda Operator


# In[ ]:




# In[ ]:




# In[ ]:

# 1. 절차 지향적인 프로그래밍 (data, function)
# 2. 객체 지향 프로그래밍 (OOP; Object Oriented Programming)
#    - Object - 상태(State == data), 행동(Behavior==function) 
# ----------------------------------------------------------
# 3. 함수형 프로그래밍
#    - Function(stateless), CommonLish(Scheme), O'Caml
#    - SICP ( "프로그래밍의 원리와 이해; 이광근" ), MIT 
#    - 1년 스터디... (!)


# In[4]:

# Class, |||||  Object == Instance


# In[5]:

# 사람 Class

# 안수찬(name: "안수찬", age: 30 + 인사하기, 먹기)


# In[6]:

# 사람 Class => A사람, B사람, C사람, D사람


# In[7]:

# 사람 Class
# A 는 객체다 ( Object ) 다.
# A 는 사람 Class 의 인스턴스(Instance) 다.


# In[9]:

{"name": "안수찬"}                    # Dict Object
                                    # Dict Class Instance
    
                                    # State: name => "안수찬"
                                    # Behavior: .items()


# In[10]:

"안수찬"  # State: 안수찬, Behavior: split, replace, format....


# In[84]:

class Person:
#     name = "Nonamed"
#     age = 0

    def __init__(self, name, age):      # __ => 파이썬에서 미리 구현된 메쏘드
        print("사람이 생성되었습니다.")
        self.name = name
        self.age = age
        
    def __add__(self, partner):
        print("{my_name} 이 {partner_name} 과 적극적으로 만난다.".format(
            my_name=self.name,
            partner_name=partner.name,
        ))
        
    def __str__(self):
        return self.name
    
    # 인사하기 => Person Class, a ( Person Class Instance )
    # 함수의 첫번째 인자로는 무조건 객체 자기 자신이 들어간다.
    def hello(self):
        print("안녕하세요, {age}살 {name} 입니다.".format(
            age=self.age,
            name=self.name,
        ))
        
    def meet(self, another):
        print("{my_name} 이라는 사람이 {another_name} 을 만났습니다.".format(
            my_name=self.name,
            another_name=another.name,
        ))


# In[85]:

a = Person("안수찬", 30)   # 객체를 생성하는 방법   
                         # Person.__init__(________________, )


# In[86]:

b = Person("정채연", 20)


# In[87]:

a.meet(b)
# 안수찬이라는 사람이 정채연을 만났습니다.


# In[88]:

a + b     


# In[90]:

print(a)


# In[91]:

a


# In[ ]:




# In[ ]:




# In[ ]:




# In[46]:

import pandas as pd


# In[47]:

df = pd.read_csv("../../students.csv", header = 0)


# In[96]:

# df => DataFrame Class Instance
#       Object


# In[48]:

df


# In[98]:

# Django 1.4 -> Django 1.5
# Function Based ----> Class  * FBV, CBV
#                     


# In[99]:

# Triangle Class ( 삼각형 )
# State: width, height
# Behavior: get_area, is_bigger_than


# In[ ]:

# a.is_bigger_than(b)   # True, False


# In[108]:

class Triangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height / 2
    
    def is_bigger_than(self, another):
        return self.get_area() > another.get_area()


# In[109]:

# 파이썬 컨퍼런스 발표
# 책
# 장고 - 튜토리얼

# 파이썬 - 1. 깐깐하게 배우는 파이썬,  <<<<<  2. 실전 파이썬 프로그래밍
# 장고 - 2. 공식 문서 ( django tutorial ), two scoops of django

# BOJ(백준 온라인 저지)
# 알고스팟 


# In[110]:

# Ruby - Convention over Configuration
# Python - Beautiful, Explicit


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



