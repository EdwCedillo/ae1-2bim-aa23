from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py

from proveedor.models import *
#from proveedor.models import EntidadProveedor
# Create your views here.

def distribuidores(request):
	"""
        Listar los registros del modelo Equipo,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # distribuidores
	mis_distribuidores = EntidadProveedor.objects.all() 
	num_distribuidores = len(mis_distribuidores)
	informacion_template = {'mis_Entidades': mis_distribuidores, 'num_entidades': num_distribuidores}
    return render(request,'distribuidores.html', informacion_template)

