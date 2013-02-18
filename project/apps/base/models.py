from django.db import models


class Pupil(models.Model):

    first_name = models.CharField('first name', max_length=30)
    middle_name = models.CharField('middle name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    birth_date = models.DateField()
    pupil_id = models.IntegerField()

    def get_classId_set(self):
        return self.classid_set.all()

    def full_name(self):
        return u"%s %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = ('Pupil')
        verbose_name_plural = ('Pupils')

    def __unicode__(self):
        return self.full_name()


class ClassId(models.Model):

    class_id = models.CharField("class", max_length=5)
    praepostor = models.ForeignKey(Pupil)

    class Meta:
        verbose_name = ('ClassId')
        verbose_name_plural = ('ClassIds')

    def __unicode__(self):
        return self.class_id
