from operation.models import *


class Clientelemarketing(Base):
    name = models.CharField(max_length=200, verbose_name='Nome')
    address = models.CharField(max_length=250, verbose_name='Endereço')
    type_client = models.IntegerField(choices=ROLE_CHOICE, verbose_name='Tipo de cliente', default=1)
    telcell = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telfix = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    status = models.BooleanField(default=True, verbose_name='Cliente ativo')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """
        Class to sort the admin and create a human-readable name for the object
        """
        verbose_name = 'Operação'
        verbose_name_plural = 'Operações'
