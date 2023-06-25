from django.contrib import admin

# Importar las clases del modelo
from proveedor.models import EntidadProveedor

# Register your models here.
# Agregar la clase Equipo para administrar desde
# interfaz de administración}
admin.site.register(EntidadProveedor)