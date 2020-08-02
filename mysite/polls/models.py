from django.db import models
class Question(models.Model):
    Question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.Question_text


class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
# Create your models here.
# Question
# Question Text
# Publish Date
#
# Choices
# Choice Text
# Number of Votes
# Link