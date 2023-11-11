from django.db import models

# Create your models here.
class CityDetail(models.Model):
    city = models.CharField(max_length=256)
    detail = models.CharField(max_length= 256)

    
class Travel(models.Model):
    # CITY_CHOICE = [
    #     ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'),
    #     ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('경상북도', '경상북도'),('경상남도', '경상남도'),
    #     ('제주도', '제주도')
    # ]
    # city = models.CharField(max_length=256, choices=CITY_CHOICE, default='경기도')
    city_detail = models.ForeignKey(CityDetail, on_delete=models.CASCADE)
 