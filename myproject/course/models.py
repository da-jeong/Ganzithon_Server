from django.db import models

# Create your models here.

# def user_photo_path(instance, filename):
#     return f'user_photos/{instance.member.pk}/{filename}'

class Course(models.Model):
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=10) #지역API 써야할듯
    # photo = models.ImageField(upload_to=user_photo_path, max_length=150, null=True)

    def __str__(self):
        return self.title


class Plan(models.Model):
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    day_num = models.IntegerField(null=True)
    time = models.CharField(max_length=10, null=True)
    place = models.CharField(max_length=20, null=True)
    memo = models.CharField(max_length=40, null=True)

