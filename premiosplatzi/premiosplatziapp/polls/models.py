from django.db import models

# Create your models here.
# name´s models always singular
# cada vez que se haga un cambio se debe hacer migration

# python3 manage.py makemigrations polls
# python3 manage.py migrate
class Question(models.Model):

    # id - Django lo hace automáticamente
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)