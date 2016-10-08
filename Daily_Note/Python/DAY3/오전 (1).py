
# coding: utf-8

# In[2]:

# 방향?
# 0, 1, 2, 3 ( == 4의 나머지 ) ( direction = _________ % 4 )


# In[3]:

# 함수 ... 를 리턴하는 함수 ( decorator )


# In[4]:

# === 함수의 실행 시간을 측정하는 함수 ===


# In[38]:

def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")


# In[75]:

import time

start_time = time.time()
hello("안수찬")                                       # 얘를 실행하기 위해서
end_time = time.time()
exec_time = end_time - start_time
print("Execute Time: {time}".format(time=exec_time))


# 1. hello => new_hello
# 2. exec time tracking 모든 함수 ... new_&&&&& 
# 3. 인자를 명시적으로 모든 함수에 대해서 정의해줘야 한다.


# In[20]:

def new_hello():
    start_time = time.time()
    hello()                                       # 얘를 실행하기 위해서
    end_time = time.time()
    exec_time = end_time - start_time
    print("Execute Time: {time}".format(time=exec_time))


# In[21]:

new_hello()


# In[ ]:




# In[44]:

def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")
    
# -------------------------
# 함수를 리턴하는 함수

def get_multiply_by(n):
    def return_function(x):              # 새로운 함수를 만들어서 리턴하자!
        return x * n
    return return_function

# ---------------------------------------------------------------
# decorator => 함수를 input 으로 받아서 => 새로운 함수를 만들어서 리턴하자.
# 함수를 받아 새로운 함수를 리턴하는 함수

def track_time(func):
    pass

# hello = track_time(hello)
hello("안수찬")                  # 1. 실행시간 까지 같이 표시되어야 한다.
                               # 2. hello 라는 함수는 input 으로 name 을 받는다.


# In[29]:

triple = get_multiply_by(3)


# In[30]:

triple(100)


# In[5]:

def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")

# ---------------------------------------------------------------
# decorator => 함수를 input 으로 받아서 => 새로운 함수를 만들어서 리턴하자.
# 함수를 받아 새로운 함수를 리턴하는 함수

def track_time(func):               # pack!
    def new_func(*args, **kwargs):  # 인자가 하나인 함수에만 동작하는 기능 => args, kwargs 로 확장!
        # print(args)                # ("hello", )
        # print(kwargs)              # {}
        start_time = time.time()
        func(*args, **kwargs)                 # hello(("안수찬", ), {}) => hello("안수찬") # unpack
        end_time = time.time()
        exec_time = end_time - start_time
        print("Execute Time: {time}".format(time=exec_time))
    return new_func

hello = track_time(hello)
hello("안수찬")                  # 1. 실행시간 까지 같이 표시되어야 한다.
                               # 2. hello 라는 함수는 input 으로 name 을 받는다.


# In[74]:

def world():
    print("Bye Bye")


# In[66]:

world = track_time(world)


# In[67]:

world()


# In[4]:

import time


# In[1]:



# ---------------------------------------------------------------
# decorator => 함수를 input 으로 받아서 => 새로운 함수를 만들어서 리턴하자.
# 함수를 받아 새로운 함수를 리턴하는 함수

def track_time(func):               # pack!
    def wrapper(*args, **kwargs):  # 인자가 하나인 함수에만 동작하는 기능 => args, kwargs 로 확장!
        # print(args)                # ("hello", )
        # print(kwargs)              # {}
        start_time = time.time()
        func(*args, **kwargs)                 # hello(("안수찬", ), {}) => hello("안수찬") # unpack
        end_time = time.time()
        exec_time = end_time - start_time
        print("Execute Time: {time}".format(time=exec_time))
    return wrapper


@track_time                      # decorator            # hello = track_time(hello)
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")


# In[12]:

# 함수의 시작을 알려주는 decorator

# ===== 함수를 실행합니다 =====
# _________________________


# In[13]:

# 함수의 끝을 알려주는 decorator

# _________________________
# ===== 함수를 종료합니다 =====


# In[158]:

def start_func(func):
    print("start_func decorator 적용 시점")
    def wrapper(*args, **kwargs):
        print("==== 함수를 시작합니다 ====")
        return func(*args, **kwargs)
    return wrapper

def finish_func(func):
    print("finish_func decorator 적용 시점!")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("==== 함수를 종료합니다 ====")
        return result
    return wrapper


# In[159]:

@track_time
@finish_func
@start_func
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")


# In[160]:

hello("안수찬")


# In[157]:

# ==== 함수를 시작합니다 ====
# 안녕하세요, 저는 안수찬 입니다.
# ==== 함수를 종료합니다 ====
# Execute TIme: __________________


# In[ ]:




# In[150]:

# Decorator


# In[151]:

# 데이터 분석 

# 서버 ( 1대 ) => 50대 ~ 100대

# 1. 데이터 수집하는 과정 ( 크롤링 )
# 2. 데이터 전처리 ( preprocess )
# 3. 데이터 분석 ( Ananlysis ) => Machine Learning, DeepLearning 
# 4. 데이터 분석 결과 ...


# In[66]:

# Notify


# In[67]:

# @send_sms
# @which_server


# In[68]:

# Web Programming!!!


# In[69]:

# Log


# In[70]:

# 함수...
# input:HttpRequest(요청) -> output:HttpResponse(응답)
# 


# In[ ]:

def home(request):
    # HTML 파일을 읽어서 보내준다.
    return response

@is_admin  ==> *args, **kwargs ( args[0] => request )
def users(request):
#     if request.user.is_admin:
#         return response
#     return 잘못된 접근입니다.
    return response


@login_required
def mypage(request):
#     if request.user:
#         return response
#     return 로그인 페이지로 redirect
    return response


# In[ ]:

# decorator function name
# decorator function docstring


# In[ ]:



