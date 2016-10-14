from django.db import models


# 유저 정보를 확장
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser \
    , BaseUserManager, PermissionsMixin

# 계정 생성을 담당하는 UserManager 모델 create
# 따로 usermanager를 만드는 이유: create_user / create_superuser 할때 필요한 info를 지정해주지만
# 그 info말고 vip정보든, 따로 관리하고싶다.
class MyUserManager(BaseUserManager):
    # create_user 나 create superuser할때 필요시하는 정보들
    def create_user(
            self,
            email,
            last_name,
            first_name,
            nickname,
            password=None):
        user = self.model(
            email = email,
            last_name = last_name,
            first_name = first_name,
            nickname = nickname,
        )
        user.set_password(password)
        # password를 암호화하기위해
        user.save()
        return user

    def create_superuser(
            self,
            email,
            last_name,
            first_name,
            nickname,
            password):
        user = self.model(
            email = email,
            last_name = last_name,
            first_name = first_name,
            nickname = nickname,
        )
        user.set_password(password) #해싱하는 작업을한다
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length =100, unique= True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=24, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    #아무나 장고 admin 에 접속하면안되닌깐 is_staff
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('last_name','first_name', 'nickname',)
    # create super user 할때 요구한
# 사용자를 판단할때 username

    # user모델에게 어떤 클래스가 manager 역할을 할것인지 알려준다
    objects = MyUserManager()
    # By default, Django adds a Manager with the name objects to every Django
    # model class. However, if you want to use objects as a field name, or if
    # you want to use a name other than objects for the Manager,
    # you can rename it on a per-model basis.
    def get_full_name(self):
        return '%s%s' % (self.last_name, self.first_name)

    def get_short_name(self):
        return self.first_name

