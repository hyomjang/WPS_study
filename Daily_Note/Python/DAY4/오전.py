
# coding: utf-8

# In[3]:

# Animal Class

# State: type(String) : "dog", "cat", "fish"
# State: weight(Integer)

# Behavior: eat() => "먹이를 먹습니다."
# Behavior: is_heavier_than(another) => True, False


# In[6]:

# "dog" 4kg ( d4 )
# "dog" 5kg ( d5 )
# "cat" 6kg ( c6 )
# "cat" 3kg ( c3 )


# In[30]:

class Animal:
    
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
        
    def eat(self, *args):                    # Polymorphism ( 다형성 )
                                             #   - Parametic Polymorhism ( overloading)
        if not args:
            print("먹이를 먹습니다.")
        else:
            print("\n".join([
                "{food}을/를 먹습니다.".format(food=arg)
                for arg
                in args
            ]))
            
        
    # d3.eat() => "먹이를 먹습니다."
    # d3.eat("소세지") => "소세지을/를 먹습니다."
    # d3.eat("소세지", "햄") => "소세지을/를 먹습니다." + "햄을/를 먹습니다."        
    def swim(self):
        print("헤엄을 친다." if self.type == "fish" else "물에 빠진다.")
        
    def is_heavier_than(self, another):
        return self.weight > another.weight
    
d4 = Animal("dog", 4)
d5 = Animal("dog", 5)
c6 = Animal("cat", 6)
c3 = Animal("cat", 3)
f1 = Animal("fish", 1)


# In[18]:

f1.swim()


# In[31]:

d4.eat()


# In[32]:

d4.eat("소세지")


# In[33]:

d4.eat("소세지", "햄", "바나나")


# In[ ]:




# In[34]:

# 상속 ( Inheritance )
# 삼각형, 사각형 

# width, height
# area => w * h / 2
# area => w * h


# In[84]:

class Shape:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def is_bigger_than(self, another):                  # Type 이 달라도 동작!
                                                        # Sub-Type Polymorphism
        if not isinstance(another, Shape):
            return "오류"
        return self.area() > another.area()
    
    def area(self):
        return "오류"
        
        
class Triangle(Shape):
    
    def area(self):                                 # Method Overriding ( 덮어쓰기 )
        return self.width * self.height / 2
    
    
class Rectangle(Shape):
    
    def area(self):
        return self.width * self.height
    
    
class Pentagon(Shape):
    
    pass
    
# is_bigger_than ...?


# In[85]:

p = Pentagon(10, 20)
p.area()


# In[86]:

rec = Rectangle(10, 20)  # 200
rec.area()


# In[73]:

for shape in [tri, rec]:
    
    print(shape.area())      # 다른 Class ( Triangle, Rectangle ) 


# In[74]:

tri2 = Triangle(10, 21)


# In[75]:

tri.is_bigger_than(rec)


# In[76]:

class Room:
    
    def __init__(self, real_area):
        self.real_area = real_area
        
    def area(self):
        return self.real_area


# In[77]:

room = Room(200)


# In[78]:

room.area()


# In[80]:

tri.is_bigger_than(room)


# In[103]:

# 1. 정확한 비교 => type
# 2. 상속? => isinstance(객체, 클래스)
# 3. 상속? => issubclass(클래스, 클래스)


# In[104]:

isinstance("dobestan", (str, int, ))


# In[ ]:




# In[ ]:




# In[108]:

class Animal():
    
    def __init__(self, weight):
        self.weight = weight
        
    def is_bigger_than(self, animal):
        return self.weight > animal.weight
    
    def eat(self):
        print("먹이를 먹는다.")


class Dog(Animal):
    
    def eat(self):                              # * Overriding ( 메쏘드 오버라이딩 )
                                                # eat(1, 2, 3...) => Method Overloading ( 메쏘드 오버로딩 )
        print("침을 흘리면서 먹는다.")


class Fish(Animal):
    pass


# In[112]:

d3 = Dog(3)
d4 = Dog(4)
f2 = Fish(2)


# In[113]:

d3.is_bigger_than(d4)


# In[114]:

d3.is_bigger_than(f2)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[115]:

# 권한


def home(request):                # Request Class => Request 객체 
    response = Response(____________________)
    return response               # Response Class => Response 객체


# 관계형 데이터베이스 ===> SQL ( Structured Query Lang ) ====> 데이터 
# ORM ( Object Relational Mapping ) :: Ruby on Rails (Django ORM <<< Python::SQL Alchemy)
# CRUD ( Create Retrieve Update Destroy )

# 클래스 => 객체 ( row 1개 => 객체 1개 ; column => attribute ; + Behavior ) => MVC Framework :: Model


# In[116]:

# Database
#    - Users: username, email, password, phonenumber
#    - Posts
#    - Chat(Messages)


# In[118]:

# User Class => User Object
# User Class ... 확장!

# SQL... => 클래스, 객체 ( SQL )
# user.send_sms(content) => User의 핸드폰번호를 바탕으로 문자 메시지를 보내는 "기능"


# In[119]:

# 디지털 마케터 => SQL
# 웹 프로그래밍 스쿨 ( 데이터베이스 ) => SQL X


# In[120]:

# 1.4 => 1.5 CBV


# In[121]:

# TemplateView Class .... TemplateView.as_function()
# Class Based View ( 55 )
# O2O => 일반적인 서비스. ... 3-4 Model, 


# In[122]:

# FBV, CBV


# In[123]:

# 상속 관계로 이루어진 55개 


# In[ ]:




# In[ ]:




# In[ ]:

@login_required
def home(request):
    return repsonse


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



