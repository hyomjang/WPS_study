
# coding: utf-8

# In[2]:

fp = open("hello.txt", "w")    # open 이라고 하는 함수 를 사용하고 있다!


# In[3]:

fp.write("hello world")


# In[5]:

fp.close()


# In[6]:

fp2 = open("./hello.txt", "r")


# In[7]:

fp2.read()


# In[8]:

fp2.close()


# In[ ]:

# Block 
# if ______:
#     ________
#     ________
    
# ______


# In[11]:

with open("hello.txt", "r") as fp:
    data = fp.read()
    print(data)
    # 현재 Code Block 내에서만 fp 라는 변수가 존재 
    # Indent 가 끝나면
    
# 여기로 나오면 => 자동으로 fp.close() 실행


# In[12]:

with open("../students.csv", "r") as fp:
    data = fp.read()


# In[13]:

data


# In[15]:

# String 에 대한 함수들


# In[19]:

data


# In[20]:

# 구조화된 데이터


# In[21]:

# Dict List


# In[22]:

[
    {"name": "안수찬", "email": "dobestan@gmail.com", "phonenumber": "..."},
    {},
    {},
]


# In[23]:

# String
# 1. split, 2. join, 3. replace, 4. format


# In[24]:

# input ===> (...) ===> output


# In[25]:

# String ====> (...split...) ===> [String, ]


# In[29]:

"dog::cat::fish".split("::")   # CSV 파일 읽기


# In[30]:

",".join(["dog", "cat", "fish"])   # CSV 파일 쓰기


# In[31]:

# TSV ( Tab Seperated Values ) => CSV


# In[32]:

data = "안수찬\tdobestan@gmail.com\t01022205736"


# In[33]:

",".join(data.split("\t"))


# In[34]:

data.replace("\t", ",")


# In[35]:

data


# In[36]:

# format ( String Formatting ... )


# In[37]:

"안녕하세요, %s 입니다." % ("안수찬", )


# In[39]:

name = "안수찬"

"%s: 안녕하세요, %s 입니다." % (name, name, )


# In[41]:

"{name}: 안녕하세요, {name} 입니다.".format(name="안수찬")


# In[42]:

"{name},{email},{phonenumber}".format(
    name="안수찬",
    email="dobestan@gmail.com",
    phonenumber="010-2220-5736",
)


# In[45]:

["안수찬1", "안수찬2", "안수찬3"]


# In[46]:

animals = []


# In[47]:

animals.append("dog")


# In[50]:

animals.append("cat")

# input ( String )
# output ( None )
# 원본 list 에다가 input 으로 받은 String 추가


# In[64]:

with open("../students.csv", "r") as fp:
    data = fp.read()  # 1. 파일 읽기
    rows = data.split("\n")    # 2. newline char(\n) 나누는 작업
                               # 각각의 row 가 element 로 들어가있음.
    students = []
    
    for row in rows:   # 각각의 row에 for 문을 돌리면서,
        fields = row.split(",")   # ["안수찬", "dobestan@gmail.com", ".."]
                                  # .csv => comma 로 구분하자.
        student = {
            "Name": fields[0],
            "Email": fields[1],
            "Phonenumber": fields[2],
        }
        students.append(student)   # List 에 append
students        


# In[60]:

# 우리가 가지고 있는 Column 에 대해서 정확히 알고 있을 때.!
# Column 에 대해서 정보가 전혀 없을때!

# => csv 파일을 읽을 수 있는 코드 작성하기!


# In[ ]:




# In[61]:

with open("../students.csv", "r") as fp:
    data = fp.read()
    rows = data.split("\n")
    elements = []
    
    columns = rows[0].split(",")

    for row in rows[1:]:
        fields = row.split(",")  # len(fields) == 4
                                 # len(columns) == 4

            
        element = {}
        
        for column_index in range(len(columns)):
            field = fields[column_index]
            column = columns[column_index]
            element[column] = field
        
        elements.append(element)


# In[62]:

elements


# In[ ]:




# In[77]:

# Function 


# In[37]:

def read_csv(filename, sep=","):
    with open(filename, "r") as fp:
        data = fp.read()
        rows = data.split("\n")
        elements = []

        columns = rows[0].split(sep)
        print(sep)
        print(columns)

        for row in rows[1:]:
            fields = row.split(sep)  # len(fields) == 4
                                     # len(columns) == 4

            element = {}

            # why? 우리가 어떤 Column 이 있는지 모른다. ( 가정 )
            # student["Name"] = fields[0]   ....     (x)
            # for 문을 돌리면서 적절한 Column 에 매칭되는 Field 값을 입력해야한다.
            # ------------------------------------------
            # for column in columns:      # 우리가 실제로 찾고자 하는 index...!
            for column_index in range(len(columns)):    # 0, 1, 2, 3
                field = fields[column_index]
                column = columns[column_index]
                
                element[column] = field
                
            elements.append(element)
            # ------------------------------------------
            
        return elements


# In[108]:

def read_lsv(filename):
    return read_csv(filename, "|")

# 굉장히 간단한 함수 => 굳이 이렇게 길게 X


# In[109]:

# lambda ... ( 익명 함수... ! )


# In[110]:

def double(x):
    return x * 2


# In[113]:

double


# In[114]:

lambda_double = lambda x: x * 2


# In[115]:

lambda_double


# In[121]:

read_lsv = lambda filename: read_csv(filename, "|")
read_tsv = lambda filename: read_csv(filename, "\t")


# In[52]:

seps = [",", ".", "::", "^"]


# In[56]:

reader = {}
for sep in seps:
    reader[sep] = lambda filename: read_csv(filename, sep)


# In[57]:

reader


# In[51]:

reader["::"]("../fruits.csv")


# In[ ]:

# Lambda 코드가 엄청 간결하고...  + Lambda Operator... ( map, filter, reduce, ... )


# In[47]:

reader[","]("../students.csv")


# In[ ]:

# is_palindrome


# In[ ]:

is_palindrome("토마토")   # True
is_palindrome("ABCDCBA")   # True
is_palindrome("Apple")   # False 
                         # 5분


# In[ ]:




# In[ ]:




# In[ ]:



