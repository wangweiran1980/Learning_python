from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, null=False, default='')
    gender = models.BooleanField(null=False, default=True)
    age = models.IntegerField(null=False, default=18)
    tel = models.CharField(max_length=32)
    pwd = models.CharField(max_length=512, null=False, default='')
    create_time = models.DateTimeField(null=False)

    @classmethod
    def verify_login(cls, username, password) -> bool:
        """验证用户登录信息."""
        if cls.objects.filter(username__exact=username, pwd__exact=password):
            return True
        return False
