from django.db import models

# Create your models here.

class Faculty(models.Model):
    def __init__(self):
        self.departments = ['accounting', 'lgst', 'real-estate', 'bepp', 'mgmt', 
        'statistics', 'fnce', 'marketing', 'hcmg', 'oid'
        ]
