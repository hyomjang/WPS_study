## Python Note


##### useful markdown
*  # ~ #####
*  * & - == dot
*  > 
*  ```sh -------```
*  [ ]: <> 

##### atom shortcut
- command + d
- command + alt + [ or ]
- command + shift + [ or ]

-

#### Argument & parameter

```sh
$ def foo(x,y):
	return x + y
  z = foo (3,6)
```
- x,y == parameter (매개변수)
- 3,6 == arguments (인자)


#### Dictionary

value 를 가지고 오는 두가지 방법

*  . get('key')
*  ['key']
*  get은 None을 return / ['']는  오류를 return

#### Class

* instance: 클래스에 의해 생성된 객체
* navi = Cat() 이렇게 만들어진 navi는 객체이다. 그리고 navi라는 객체는 Cat의 인스턴스이다. 즉, 인스턴스라는 말은 특정 객체(navi)가 어떤 클래스(Cat)의 객체인지를 관계 위주로 설명할 때 사용된다. 즉, "navi는 인스턴스" 보다는 "navi는 객체"라는 표현이 어울리며, "navi는 Cat의 객체" 보다는 "navi는 Cat의 인스턴스"라는 표현이 훨씬 잘 어울린다.
* self 는 class의 의해 생성된 instance
* __init__ --> "인스턴스를 만들 때 항상 실행"
* Method == class 안에 있는 함수 (def)
* 클래스에 의해서 생성된 객체들은 다른 객체들과 완전히 다른 저장 공간을 가지고 독립적으로 동작한다는 것을 잊지 말자!


> Class Overloading

상속을 받은 클래스의 method를 다른 역할을 하게하려면?

* 메소드의 이름을 동일하게 다시 구현하고 함수를 작성


#### Decorator

* 함수를 input으로 받아서 -> 새로운 함수를 만들어서 리턴
* func(func(func(x)))

#### Memoization or caching

- 불필요한 작업을 최소화 시키기 위해 한번 계산한 결과를 사전에 저장했다가, 계산 결과가 있으면 바로 꺼내서 보여주는 식이다 (재귀 호출을 막는 방식)
- [Memoization link]


#### Interator & Generator
-
-

### 내장함수

##### isinstance
* isinstance(object, class)
* 첫번째 인수로는  인스턴스, 두번째 인수로 클래스 이름

```sh
$ class Person: 
	pass
...
a = Person()
isinstance(a, Person)
True
```
```sh
$ b = 3
isinstance(b, Person)
False
```

### Regular Expression (정규표현식)
-
* **\d** - 숫자와 매치, [0-9]
* **\D** - 숫자가 아닌 것과 매치, [^0-9]
* **\s** - whitespace 문자와 매치, [ \t\n\r\f\v]. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
* **\S** - [^ \t\n\r\f\v]
* **\w** - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9]
* **\W** - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9]
* **\b** - boundary ('\b**name**\b')
* **\A & \Z**

-
**Dot (.)** 

* a.b
* "aab" -- match
* "abc" -- not

**반복 (*) (+)**

* * 나 + 앞에 있는 문자는 무한으로 반복될 수 있다
*  * 는 0번 반복    
*  + 는 최소 1번 이상 반복 

**{m} & {m,n}**

* m만큼 무조건 반복
* m에서 n 만큼 반복 가능


**컴파일 된 패턴 객체의 4가지 메소드**

```sh
Match() - 처음부터 Match 되는지
Search() - 전체를 검색해서 정규식과 매치되는지
findall() - 매치되는 모든 문자열 리스트로 리턴
finditer() - iterator 객체로 리턴
```
**컴파일 옵션**

```sh
DOTALL(S) - (.) 이 줄바꿈 문자를 포함하여 모든 문자와 매치
IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션)
VERBOSE(X) - (정규식을 보기 편하게, 주석) 
```
**Grouping**

* () .group(0-9)
* (?p< name >\w+)


**Lookahead Assertions**

* (?=...) 
* (?!...)

```sh
# 파일명.확장자 의 bat의 확장자만 선택
.*[.](?!bat$).*$
.*[.](?!bat$|exe$).*$

```

**sub 메서드**

```sh
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")

print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

010-1234-1234 park
```
* 이름 +전화번호를 ,, 전화번호 + 이름으로 바꾸는 예

<Link>

[Memoization link]: <http://soooprmx.com/wp/archives/5149>