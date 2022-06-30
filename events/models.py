from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.category


class Organizer(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=200, blank=False)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    link = models.CharField(max_length=200, blank=False)
    # categories = models.ManyToManyField(Category)
    # eventOrganizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('title', 'link')

    def __str__(self):
        return self.title
