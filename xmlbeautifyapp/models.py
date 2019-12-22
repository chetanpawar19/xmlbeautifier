from django.db import models

class Main(models.Model):

    comment = models.CharField(max_length=150)

    class Meta:
        db_table = 'tb_xml'
