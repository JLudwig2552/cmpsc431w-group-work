from django.db import models


class Question(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)