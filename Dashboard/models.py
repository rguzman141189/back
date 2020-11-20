from django.db import models

class DashboardModel(models.Model):
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
