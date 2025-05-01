from django.db import models
from decimal import Decimal, InvalidOperation
class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date=models.DateField()
    genre=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    image=models.ImageField(upload_to='media/',null=True,  blank=True)
    video=models.TextField()
    novedades = models.TextField(null=True, blank=True)
    oferta = models.TextField(null=True, blank=True)
    
# Create your models here.
    def _str_(self):
        return self.title
    
    
    @property
    def precio_con_oferta(self):
        try:
            # Extrae solo números y punto decimal del campo oferta
            descuento_texto = ''.join(c for c in self.oferta if c.isdigit() or c == '.')
            descuento = Decimal(descuento_texto)
            return round(self.price * (1 - descuento / 100), 2)
        except (InvalidOperation, TypeError, AttributeError):
            return self.price
