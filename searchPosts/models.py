from django.db import models


# Create your models here.

class PostData(models.Model):
    language = models.CharField('语言', max_length=30)
    city = models.CharField('城市', max_length=20)
    company = models.CharField('公司', max_length=30)
    scale = models.CharField('规模', max_length=15)
    xueli = models.CharField('学历', max_length=10)
    lat = models.FloatField('纬度', max_length=15)
    longitude = models.FloatField('经度', max_length=15)
    post = models.CharField('职位', max_length=20)
    salary = models.CharField('薪资', max_length=10)
    salary_min = models.IntegerField('最少薪资', default=0)
    # salary_max = models.IntegerField('最多薪资', max_length=10)
    exp = models.CharField('工作经验', max_length=10)
    exp_min = models.IntegerField('最低工作经验', default=0)
    welfare = models.CharField('福利', max_length=30)
