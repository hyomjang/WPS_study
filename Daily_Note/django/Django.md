## Django Day 1

* mv 폴더명 바꾸기
	* mv 예전폴더명 바꿀폴더명
	* mv blog project-blog
	* 
* pwd
* rm -rf .
* ls -al --> 안보이는 파일도 보여짐

* django-admin startproject blog

* python manage.py startapp post
* python manage.py makemigrations
  * 하면 no change detected 라고 나옴
  * settings.py에서 installed_apps에 'post'설정을 줘야된다

* python manage.py runserver

* models.py에서 변경되었을때 manage.py migrate한다
*  db로 보내는 게 migrate
*  쌓인 데이타를 다루는게 orm
* 	* Post.objects.all()
*  	- 여기 모델에 있는 모든 데이터를 불러온다
*   djanggo template 에는 {}안에 for문을 
brew install pyenv
pyenv install 3.4.3
pyenv virtualenv 3.4.3 fc-blog

10/5

**html 파일에서 {{ post.description }}**

* 여기서 dot . aren't used only for attribute lookup
* They also can do dictionary-key lookup, index lookup, function calls

**Staticfiles**

* settings.py
	* STATICFILES_DIRS-  static file 위치한 경로 directory 설정
	* STATIC_URL 
		* 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
		* 실제 파일이나 디렉터리가 아니며 이용자 마음대로 정해도 무방
	* STATIC_ROOT 
		* Django project에서 사용하는 모든 정적파일을 모아넣는 경로 

> manage.py findstatic -> STATICFILES_DIRS에 설정한 경로에서 지정한 정적 파일을 찾는다.

* findstatic 명령어로 탐색되는 정적 파일 경로에 static_URL 경로를 합치면 실제 웹에서 접근 가능한 URL
	*	ex) http://127.0.0.1:8000/static/css/post_list.css

### Django Project  

* **include()** chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing
* **Foreignkey** each Choice is related to a single Questions
	* ex) models.ForeignKey(Question) 

```sh
$ python manage.py sqlmigrate polls 0001
$ python manage.py check
```
The **sqlmigrate command** doesn’t actually run the migration on your database - it just prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

* Run python manage.py makemigrations to create migrations for those changes
* Run python manage.py migrate to apply those changes to the database.
* get_object_or_404()



**Difference between render, render_to_response, direct_to_template**

	
	
##DAY2

* include를 사용하는 url에는 맨뒤에 $를 사용하지않는다
* mysite urls.py 에서 polls 를 지정했기때문에 polls.urls.py url이 ^$이여도 polls로 지정이된다
* Question.objects.order_by('-pub_date') ---내림차순
* pub_date' ---오름차순
* **/**polls/ ----> '/' 는 루트부터 시작한다라는뜻
	* http://127.0.0.1:8000/polls/ 	
* loader.get_template (index.html)
	*  loader가 app내에있는 template 을 찾아서 (index.html)를 불러준다
*  primary key == 똑같은 name을 가지지만 id는 각 data당 하나의 고유의 number를 받기때문에 ,, 지정하기 위해 primary key 를지정
*  template 에서는 question.choice_set.all() 을 사용할때 ()를**안한다**
*  template에는 question_id 가 아닌 question.id 를사용한다
	* template 에는 (.) 형식만 사용 가능하다 
*  reverse : template --? **{ %url %} tag를 사용**
			* views.py 에는 **reverse('polls:result')  **
			* 	
* django forloop counter - {%for in  %} {%end in %} 안에 사용 
	* for 문도는 횟수에 따라 숫자를 count (기본적으로 1부터시작
	* 0부터 시작하려면 forloop 0	 	


## Day 3
###Models

primary key 지정

* num = models.**AutoField(primary_key = True)**
* blank - 장고에서 다룸   null- db에서 처리
	* 둘다 default= false -->blank나  null을하면 error를 띄운다.
*  p = Person(name="Fred Flintstone", shirt_size="L")
	* p.save()
	* p.shirt_size
		'L'
	* p.get_shirt_size_display()
'Large'
* objects.create() 하면 save()안해도 저장됨
* primary key를 지정하면 원래 값을 바꿔도 pk지정한 값은 변경되지않음
	* 다른  id에 생성 



## Day 4

추상 클래스 (Abstract Class)

(Query)
**get**

- 1개만 가지고온다
- data가 두개이상이면 error

**filter**

- 2개이상의 data를 가지고온다

**__ <-는 filter instance 뒤에 붙여서 꾸며준다**

**__exact**

> Entry.objects.get(headline__exact = 'Cat bites dog')


**__iexact**

* case- insensitive match
> Blog.objects.get(name__iexact = 'beatles blog')
>

**__contains**

**__gt**

* greater than
> Entry.objects.filter(id__gt = 4)

__startswith = '', __endswith = '', __lt = , __lte = 


**F expressions**

from django.db.models import F
> Entry.objects.filter(n_comments__gt = F('n_pingbacks')*2)
* 특정 모델 필드랑 다른 필드 값 비교할때 쓴다
* 필드를 비교

Q objects

from django.db.models import Q
> and 나 or 를 사용할때 양쪽 비교값을 비교할때 Q로 묶는다


```sh
Blog.objects.filter(entry__headline__contains='', entry__pub_date__year=2008)
```
* 

```sh
Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
```
* 두개의 차이점은 -> 첫번째는 lennon과 2008을 동시에 filter하고 두번째는 lennon을 filter 하고 나중에 2008 을 filter 한다
* 만약 lennon filter를 해서 100개중 20개가 남으면나중에 20개중에 2008 을 filter 한다

* block / extends 

 base.html 을 따로 베이스로 만들고 안에 컨텐츠들만 바뀐다했을때 다른 html 파일을 만들어서 컨텐츠만 따로 관리( extends base.html )



* {{post.text|linebreaksbr}}	
	* 줄바꿈을

	
	
	 
```sh
HttpResponseRedirect(reverse('polls:results', args=(question.id,)))	
```
====
```sh
return redirect('view이름' = URL pattern namespace + name or the callable view object, question_id = question.id)	 
```

* ModelForm
	*	모델에 정의한 field들을 참조하여 모델 폼을을 만들어주는 역할을한다.
```sh
class PhotoForm(forms.ModelForm): 	
	class Meta:
		model = Photo
		fields = ['title','image','description']


* LogIN
	* 내가 네이버로그인을하고 네이버는 다른사이트를 불러올때 계속 로그인인 상태를 보여준다. 이 각각은 연결 되어있지않다. 제가 요청을 한번보내면 받은사람은 다시보내고 그리고 다시한번 요청을 보낼때 서버는 내가 로그인이 되어있다는 사실을 알아야한다.
		* session 이란 서버가 해단 서버로 request(접근한) 클라이언트를 식별하는 방법	
		* 이것을 session으로 처리를한다. 특정한 key 값을 서버와 클라이언트 쪽에서 동시에 받는다. USER가 로그인을 할때 서버쪽에서  어떤 특정한 key값을 준다. 이 유저는 이key값과 mapping된다라고 서버는 처리를한다. 그리고 이 key값을 던져주면 클라이언트는 이key값을 가지고있는다. (브라우저에는 쿠키쪽에 넣어서 그 특정한 문자를 가지고있는다) 해당사이트를 활동할때 그 쿠키값을 계속 전달을해준다 서버는 그 문자를 받으면 '아 너가 걔야' 하면서 요청을 처리해준다.
		* auth_login에서 session id를 만들어주고 middleware에서 session id 를 처리를해주는역할을하게한다

		
* command+shift+F
	* find and replace all


* Messages framework
	* 글삭제했을때, 로그인 성공할때 잠깐 팝업뜨고 사라지는것을 사용할때 
	*  

* Unique
	* 한번field에 들어가면 중복 입력 불가능	


* AUTH_USER_MODEL = 'member.MyUser'
* BaseUserManager
	* create_user& create_superuser 를 가지고있고
	* create_user 와다르게 superuser로 생성할때는 무조건 password를 provide 해야한다 

* HASH
	* 비밀번호는 암호화를 통해 (특정화 함수를 통해 고정적인 


