from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>= timezone.now()-datetime.timedelta(days=1)
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.Choice_text
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)