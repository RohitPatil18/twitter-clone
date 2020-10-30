from django.db import models

 
class Gender(models.Model):
    """
    Table to store master data of genders 
    """
    title = models.CharField(max_length=25, unique=True)

    class Meta:
        db_table = 'mst_gender'

    def __str__(self):
        return self.title


