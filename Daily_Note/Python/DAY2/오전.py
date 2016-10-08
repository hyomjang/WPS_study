
# coding: utf-8
# 1. n input 을 받아서 n 개의 짝수 리스트를 만드는(return) 함수
# 100 => [0, ..., 198]

result = []
n = 100
for i in range(n):
    # ----------------- 2 hint: condition .. if even? append
    element = i * 2
    result.append(element)
len(result) == n

# ---

def get_even_list(n): 
    result = []
    for i in range(n):
        element = i * 2
        result.append(element)
    return result
# In[10]:

# 2. n input 으로 받아서, n 보다 작은 짝수 리스트를 만드는 함수 
# 100 => [0, ..., 98]

result = []
n = 100          # result = [0, ..., 98] (len(result) == 50)

for i in range(n):
    if i%2 == 0:
        result.append(i)

def is_even(n):
    return i%2 == 0
    # even => True
    # odd => False
    # 참 => _____________, 거짓 => _________________
    
for i in range(n):
    if is_even(i):
        result.append(i)


# In[11]:

# [참일때의 값] if [조건] else [거짓일때의 값]


# In[17]:

# 3. 3의 배수, 5의 배수 
# 100 element 가 들어있는 list 2개

# list #1: ["", "", "fast", "", "", "fast", ]
# list #2: ["", "", "", "", "campus", ]

# -------------------------------------------

# list => ["", "", "fast", "", "campus", "fast", ... "fastcampus", ...]


# In[23]:

result1 = []
n = 100

for i in range(n):
    # i + 1 ( 3의 배수 ) => "fast"
    element = "fast" if (i+1)%3==0 else ""
    result1.append(element)
    
    
result2 = []
for i in range(n):
    element = "campus" if (i+1)%5==0 else ""
    result2.append(element)


# In[36]:

result = []
n = 100

for i in range(n):
    element = ("fast" if (i+1)%3==0 else "") +        ("campus" if (i+1)%5==0 else "")
    result.append(element)


# In[38]:

# n 까지의 소수를 구하는 함수 ( n 포함 X ) => [2, 3, 5, 7, 11..., 97]


# In[39]:

# 짝수 
# --- main
# --- is_even?


# In[43]:

# 소수
# --- main
# --- is_prime?


# In[50]:

for i in range(2, 5):
    pass


# In[1]:

def is_prime(n):
    """
    n 이 소수인지, 아닌지 판별하는 함수
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

assert is_prime(2) == True
assert is_prime(4) == False
assert is_prime(100) == False


# In[2]:

is_prime(3)


# In[13]:

n = 100
result = []

for i in range(2, n):
    if is_prime(i):
        result.append(i)
result


# In[74]:

# function args, kwargs ( pack, unpack )


# In[75]:

# 3 -> "fast", 5 -> "campus"


# In[17]:

def get_awesome_list(n, rule1, rule2):
    result = []
    for i in range(n):
        element = ""
        # --------------------------------------
        for rule in [rule1, rule2]:  
            div, text = rule
            element += text if (i+1)%div == 0 else ""
        # --------------------------------------
        result.append(element)
    return result


# In[18]:

get_awesome_list( 100, (3, "fast"), (5, "campus") )


# In[100]:

# ["", "", "fast", "", "campus", ...]


# In[101]:

n = 100


# In[106]:

# n = n + 10
n += 10   # n = n + 10


# In[108]:

# get_sum
# get_max


# In[5]:

def get_awesome_list(n, rule1, rule2):
  result = []
  for rule in [rule1, rule2]:  
          div, text = rule
          element += text if (i+1)%div == 0 else ""


# In[6]:




# In[ ]:



