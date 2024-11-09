from django.db import models

# Create your models here.

class Author(models.Model):
    id =models.AutoField(primary_key=True,verbose_name='作者编号')
    username = models.CharField(max_length=50,verbose_name='登录账号')
    password = models.CharField(max_length=50,verbose_name='登录密码')
    # email = models.EmailField(max_length=50,verbose_name='邮箱')
    realname = models.CharField(max_length=20,verbose_name='作者姓名')
    class Meta:
        verbose_name_plural = '作者'
    def __str__(self):
        return self.realname