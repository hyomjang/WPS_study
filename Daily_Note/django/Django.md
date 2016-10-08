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













