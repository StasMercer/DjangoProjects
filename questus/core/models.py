from django.db import models

# Create your models here.

class QuestLeaf(models.Model):
    ROLE_CHOICES = (('1', 'question'),
                    ('2', 'leaf'))

    type = models.CharField(choices=ROLE_CHOICES, max_length=1, default='2')

    text = models.TextField()

    next = models.ManyToManyField('QuestLeaf', related_name='next_leaf', blank=True)

    params = models.ManyToManyField('Param', related_name='leaf_param', blank=True)

    raise_param = models.ManyToManyField('Param', related_name='leaf_raise', blank=True)

    def __str__(self):
        return 'obj(id = %i text = %s)' % (self.id, self.text)

class Param(models.Model):

    name = models.CharField(max_length=50)


class ParamsSet(models.Model):
    params = models.ManyToManyField('Param', related_name='param_in_set', blank=True)

