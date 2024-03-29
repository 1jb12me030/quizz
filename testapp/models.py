from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import DateTimeField
from django.utils import tree
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
   
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#here updated is parent class
class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name=("_Last Updated"), auto_now=True)

    class Meta:
        abstract = True

class Question(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advance')),
        (4, _('Expert'))
    )

    Type = (
        (0, _('Multple Choice')),
    )


    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=Type, default=0, verbose_name= _("Type of Question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

 #this class is for Answer and updated is inherited here   

class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text