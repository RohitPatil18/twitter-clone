from django.db import models


class Country(models.Model):
    """
    Table to store master data of countries 
    """
    country_name = models.CharField(max_length=100, unique=True)
    country_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mst_country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name