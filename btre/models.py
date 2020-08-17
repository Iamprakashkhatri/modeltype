from django.db import models

class RealtorManager(models.Manager):
    def get_queryset(self):
        return super(RealtorManager,self).get_queryset().filter()[:1]


class Realtor(models.Model):
    name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200,default='')
    first_name=models.CharField(max_length=300,default='')

    realtor=RealtorManager()

    def __str__(self):
        return self.name

class Listing(models.Model):
    name=models.CharField(max_length=300)
    realtor = models.ForeignKey(Realtor, related_name='listings',on_delete=models.CASCADE)

    def __str__(self):
        return self.name