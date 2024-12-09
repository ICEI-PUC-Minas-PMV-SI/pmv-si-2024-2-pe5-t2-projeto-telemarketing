from django.db import models

ROLE_CHOICE = (
    (1, 'PESSOA FÍSICA'),
    (2, 'EMPRESA')
)

class Base(models.Model):
    """
    Abstract Class used in other classes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        This class makes the class Base be abstract
        """
        abstract = True

from .operationdb import Clientelemarketing