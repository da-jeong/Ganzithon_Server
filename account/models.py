from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token
import uuid


class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, username, password=None):#  nickname, 

        if not username:
            raise ValueError('must have usernames')
        user = self.model(
            #email = self.normalize_email(email),
            username = username, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, username, password=None):
        user = self.create_user(
            password = password,
            username = username
        )
        token = Token.objects.create(user=user)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=128, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
       return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'username'
    # 필수로 작성해야하는 field
   # REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.userId:
            self.userId = uuid.uuid4()
        super().save(*args, **kwargs)