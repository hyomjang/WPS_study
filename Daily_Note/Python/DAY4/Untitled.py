
# coding: utf-8

# In[144]:

class Awesome():
    
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        print("Getter Called")
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def my_instance_method(self):        # Instance Method 
                                         # 첫번쨰 인자는 무조건 Instance ( =self )!
        return self
    
    @classmethod
    def my_class_method(cls):            # Class Method
                                         # Class, Instance 모두 부를 수 있다!
                                         # But, 첫번째 인자가 무조건 Class 자기자신 ( 혹은 인스턴스의 클래스 )
                                         #                       ( = cls )
        return cls
    
    @staticmethod
    def my_static_method():              # Static Method ( Class/Instance 와 무관하게 )
                                         # Behavior
        return "static"


# In[145]:

awesome = Awesome("name")


# In[146]:

awesome.name = "dobestan"


# In[147]:

awesome._Awesome__name


# In[ ]:




# In[128]:

class User:
    
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        
    @property
    def full_name(self):
        return self.last_name + self.first_name


# In[132]:

user = User("안", "수찬")


# In[133]:

user.last_name


# In[134]:

user.first_name


# In[135]:

user.full_name


# In[ ]:




# In[4]:

# Class PySnail

# n x n 초기화
# 그려주는 기능
# 예쁘게 출력해주는 기능

