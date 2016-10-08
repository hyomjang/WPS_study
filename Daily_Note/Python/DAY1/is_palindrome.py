
# coding: utf-8

# In[1]:

# is_palindrome("토마토")   # True
# is_palindrome("ABCDCBA")   # True
# is_palindrome("Apple")   # False 
#                          # 5분


# In[15]:

data = "apple"


# In[16]:

#     a     p    p    l     e
#     0     1    2    3(==n-1-1)     4(== n-1-0)


# In[17]:

# i <==> n-1-i


# In[20]:

def is_palindrome(string):
    length = len(string)
    for i in range(len(string)):
        left = string[i]
        right = string[length-1-i]
        
        if left != right:
            return False
    return True


# In[23]:

def is_palindrome(string):
    return string == string[::-1]


# In[26]:

is_palindrome = lambda x: x == x[::-1]


# In[27]:

is_palindrome("apple")


# In[28]:

is_palindrome("토마토")


# In[29]:

# 파이썬 개발 환경 설정
#   1. pyenv
#   2. virtualenv
#   3. autoenv 
# -----------------
# Python Basic (1) - Data Types, Conditional Statement(if, elif, else )
#                    Loops, File I/O, Function ( read_csv )
#                    Lambda 
# -----------------
# Python Basic (2) - 파이썬을 가지고 간단한 문제들 ( is_palindrome... )
#                  - List Comprehension
#                  - Lambda Operator
#                  - Function Advanced ( *args,**kwargs,  ... )
#                  - Class ....


# In[ ]:

# Ubuntu 14.04(16.04) => pyenv, virtualenv, autoenv + project 2-3
# PEP8
# PEP0 - The Zen of Python
# 복습...

