from django.db import models

# Create your models here.

class Entrada(models.Model):
    CostoEntrada = models.PositiveIntegerField()
    ENTRADAS = (('S' , 'Standard'),('V' , 'VIP'))
    entrada = models.CharField(max_length=1, choices=ENTRADAS , default='S')

    def __str__(self):
        return self.entrada

class Escenario(models.Model):
    TECHO = (('S' , 'Si'),('N' , 'No'))
    ZONAS = (('N' , 'Norte'),('S' , 'Sur'),('E', 'Este'),('O', 'Oeste'))
    NombreEscenario = models.CharField(max_length=35)
    techado = models.CharField(max_length=1, choices=TECHO , default='N')
    zona = models.CharField(max_length=1, choices=ZONAS , default='N')

    def __str__(self):
        return self.NombreEscenario

class Artista(models.Model):
    tipo = (('H', 'Headliner') , ('S', 'Support') , ('L', 'Local'))
    Escenario  = models.ForeignKey('Escenario', null =    False , blank   =  False , on_delete=models.CASCADE)
    nombreArtista = models.CharField(max_length=35)
    tipo_Artista = models.CharField(max_length=1, choices=tipo, default='?')
    descripcion = models.CharField(max_length=800, blank = True, default='')
    dni = models.CharField(max_length=12)
    generoMusical = models.CharField(max_length=35)
    fechaPresentacion = models.DateField()
    emailContacto = models.EmailField()


    def __str__(self):
        return self.nombreArtista

"""class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    apellidoUsuario = models.CharField(max_length=50)
    correoUsuario = models.EmailField()
    telefono = models.IntegerField()
    contraseña = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=true)"""
