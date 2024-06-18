from django.db import models

class Groups(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    owners = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Cfps(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, db_column='group_id')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=100)
    tags = models.CharField(max_length=15)
    begin = models.CharField(max_length=50)
    close = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Events(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, db_column='group_id')
    name = models.CharField(max_length=255)
    talks = models.CharField(max_length=50)
    cfp_id = models.ForeignKey(Cfps, on_delete=models.CASCADE, db_column='cfp_id')
    venues = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tags = models.CharField(max_length=15)
    begin = models.CharField(max_length=50)
    close = models.CharField(max_length=50)

    def __str__(self):
        return self.name