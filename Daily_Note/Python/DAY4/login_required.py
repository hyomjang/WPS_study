
# coding: utf-8

# In[ ]:

# login_required   유저가 로그인 되었는지              @login_required
# is_admin         유저가 관리자인지                  @is_admin


# User Class :: username, is_admin


# Request    :: user instance ( user O => 로그인 O ; user X => 로그인 X ), url(string)
#    request = Request()
#    request.user 
#   
# Response   :: body(string)


class User:
    
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin
        

dobestan = User("dobestan")
admin_user = User("admin", is_admin=True)


# In[6]:

class Request:
    
    def __init__(self, url, user=None):
        self.url = url
        self.user = user
        

class Response:
    
    def __init__(self, body):
        self.body = body
        
    def __repr__(self):
        return "Response :: {body}".format(body=self.body)


# In[7]:

def mypage(request):                            # decorator :: login_required !!!
    return Response("성공적으로 MyPage 에 접속했습니다.")


# In[ ]:

request = Request("/mypage/","dobestan")
mypage(request)


# In[9]:

request = Request("/mypage/")
mypage(request)


# In[10]:

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            response = func(request, *args, **kwargs)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper


# In[11]:

@login_required
def mypage(request):                            # decorator :: login_required !!!
    return Response("성공적으로 MyPage 에 접속했습니다.")


# In[12]:

def admin(request):                            # decorator :: login_required !!!
    return Response("성공적으로 Admin 에 접속했습니다.")


# In[13]:

def is_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user and request.user.is_admin:
            response = func(request, *args, **kwargs)
        else:
            response = Response("관리자 권한이 필요합니다.")
        return response
    return wrapper


@is_admin                 # "로그인이 필요합니다." user => "관리자 권한이 필요합니다."
@login_required
def admin(request):                            # decorator :: login_required !!!
    return Response("성공적으로 Admin 에 접속했습니다.")


# In[14]:

request = Request("/admin/")
admin(request)                          # 로그인이 필요합니다.
                                        # 권한 Class, Response(권한...)


# In[15]:

request = Request("/admin/", user=dobestan)
admin(request)


# In[16]:

request = Request("/admin/", user=admin_user)
admin(request)


# In[17]:

# RESTful API


# In[18]:

# 사실상의 표준; de facto ...


# In[19]:

import requests


# In[20]:

# Request :: HTTP Method(GET, POST, PATCH, PUT, DELETE), URL, Headers
response = requests.get("http://www.naver.com/")


# In[21]:

response

# __repr__
# return "<Response [{status_code}]>".format(status_code=response.status_code)


# In[22]:

response.status_code  # 200 OK ( 404 NOT FOUND, 301 REDIRECT )


# In[23]:

"윤보미" in response.text


# In[24]:

# "realrank" 라고 하는 "id" 를 가진 "ol" 태그
# 그 안에 있는 li ( 10개 )

# CSS Selector
#                                            ol#realrank li


# In[25]:

# response.text 의 데이터를 잘 가공해서 우리가 원하는 데이터만 추출


# In[26]:

# html parsing


# In[27]:

from bs4 import BeautifulSoup


# In[28]:

result = BeautifulSoup(response.text, "html.parser")         # string => BeautifulSoup


# In[29]:

elements = result.select("ol#realrank li")


# In[30]:

len(elements)


# In[31]:

element = elements[0]


# In[32]:

element.select_one("a").attrs["title"]

[
    element.select_one("a").attrs["title"]
    for element
    in elements[:-1]
]


# In[ ]:




# In[33]:

# 1. 정적인 사이트 ( Server Rendering ) - 네이버 메인페이지, 네이버 블로그 검색결과, 일반 홈페이지 
# 2. 동적인 사이트 ( Client Rendering :: API, Ajax ) - 직방, 다방, 요기요, ( + 모바일 앱 )
# 3. 한국형 사이트 ( Javascript ) - 사내 인트라넷, 아주 옛날 공공기관의 데이터를 뿌려주는 웹 페이지
# 4. 한국형 사이트 ( iFrame ) - 네이버 카페, 옛날 사이트

# -----------------------------------------------------------------------------------

# x3


# In[34]:

# 사이트 => 이걸 어떻게 접근해야할까?


# In[35]:

# HTTP Request => Parsing ( 1번 )


# In[36]:

# Django Framework + Django Rest Framework 


# In[ ]:




# In[37]:

# CreateView, ListView, DetailView, TemplateView, UpdateView
# 1.0 => 2.0


# In[ ]:




# In[38]:

# Iterator, Generator, 


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



