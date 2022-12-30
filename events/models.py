from django.db import models

class Event(models.Model):
    CATEGORY = (
        ('Smiles', 'Smiles'),
        ('Laughter', 'Laughter'),
        ('Crazy', 'Crazy'),
        ('Food', 'Food'),
        ('Outside', 'Outside'),
    )
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )

    RATING = (
        ('Highly recommended', 'Highly recommended'),
        ('Fun for the whole family', 'Fun for the whole family'),
    )

    title = models.CharField(max_length=200, blank=False, unique=True )
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
    startDate = models.DateField(auto_now_add=True, null=True)
    endDate = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=200, blank=False, unique=True)
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATEGORY)
    rating = models.CharField(max_length=200, null=True, blank=True, choices=RATING)

    objects = models.Manager()
    
    def __str__(self):
        return self.title