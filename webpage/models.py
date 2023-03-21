from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=10)
    age = models.IntegerField()
    
    # Shows only fname & lname in the database
    def __str__(self):
        return self.fname + ' ' + self.lname
    
class Question(models.Model):
    question_id = models.IntegerField()
    question = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    
class Question_choices(models.Model):
    choice_id = models.IntegerField()
    is_right_choice = models.BooleanField(default=False)
    choice = models.CharField(max_length=50)
    attemptsleft = models.IntegerField()
    
class Sms1(models.Model):
    sender = models.BooleanField(default=False)
    main = models.BooleanField(default=True)
    date = models.BooleanField(default=False)
    link = models.BooleanField(default=True)