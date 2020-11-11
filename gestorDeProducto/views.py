from django.shortcuts import render
from gestorDeProducto.models import Sucursal, Marca, Tipo, Producto, Anime

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def registro(request):
    nombre = ""

    if request.method == "POST":
        nombre = request.POST[""]


    contexto = {}
    return render(request, 'registro.html', {})

def sucursal(request):
    mensaje = ""
    lista = {}
    item ={}

    if request.method == "POST":
        #VALIDAR DATOS ANTES DE GUARDAR
       id = int("0" + request.POST["txtId"])
       nombre = request.POST["txtNombre"]
       direccion = request.POST["txtDireccion"]
       telefono = request.POST["txtTelefono"]
       encargado = request.POST["txtEncargado"]

       if 'btnGrabar' in request.POST:
           #Modificamos los datos de una sucursal mediante el id
           if id < 1:
                Sucursal.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, encargado=encargado)
           else:
                item = Sucursal.objects.get(pk = id)
                item.nombre = nombre
                item.direccion = direccion
                item.telefono = telefono
                item.encargado = encargado
                item.save()
                item = {}
           mensaje = "Operacion realizada con éxito!"
       elif 'btnListar' in request.POST:
           #lista = Sucursal.objects.all()
           lista = Sucursal.objects.filter(nombre__contains = nombre)

       elif 'btnBuscar' in request.POST:
           item = Sucursal.objects.get(pk = id)

       elif 'btnEliminar' in request.POST:
            item = Sucursal.objects.get(pk = id)
            item.delete()
            mensaje = "El regitro " + item.nombre + " fue eliminado con exito!"
            item = {}
            


    contexto = {'mensaje' : mensaje, 'lista' : lista, 'item' : item}
    return render(request, 'sucursal.html', contexto)


def producto(request):
    mensaje = ""
    lista = {}
    item ={}
    cmbAnime = Anime.objects.all()
    cmbMarca = Marca.objects.all()
    cmbTipo = Tipo.objects.all()
    errores = {}

    if request.method == "POST":
        #VALIDAR DATOS ANTES DE GUARDAR
       id = int("0" + request.POST["txtId"])
       idanime = int("0" + request.POST["cmbAnime"])
       idmarca = int("0" + request.POST["cmbMarca"])
       idtipo = int("0" + request.POST["cmbTipo"])
       codigo_producto = int("0" + request.POST["txtCodigo"])
       nombre = request.POST["txtNombre"]
       descripcion = request.POST["txtDescripcion"]
       stock = int("0" + request.POST["txtStock"])
       precioCosto = int("0" + request.POST["txtprecioCosto"])
       precioVenta = int("0" + request.POST["txtprecioVenta"])

       if 'btnGrabar' in request.POST:
           #Modificamos los datos de una sucursal mediante el id
           anime = buscarPorId(Anime, idanime)
           marca = buscarPorId(Marca, idmarca)
           tipo = buscarPorId(Tipo, idtipo)

           if anime is None:
               errores['cmbAnime'] = "No selecciono el anime"
           elif marca is None:
               errores['cmbMarca'] = "No selecciono la marca"
           elif tipo is None:
               errores['cmbTipo'] = "No selecciono el tipo"
          
           else:
               if id < 1:
                   Producto.objects.create(anime=anime, marca=marca, tipo=tipo, codigo_producto=codigo_producto, nombre=nombre, descripcion=descripcion, stock=stock, precioCosto=precioCosto, precioVenta=precioVenta)
                   mensaje = "El producto fue guardado correctamente!"
               else:
                   item = Producto.objects.get(pk = id)
                   item.anime = anime
                   item.marca = marca
                   item.tipo = tipo
                   item.codigo_producto = codigo_producto
                   item.nombre = nombre
                   item.descripcion = descripcion
                   item.stock = stock
                   item.precioCosto = precioCosto
                   item.precioVenta = precioVenta
                   item.save()
                   item = {}
                   mensaje = "Operacion realizada con éxito!"
       elif 'btnListar' in request.POST:
           lista = Producto.objects.all()
           #lista = Producto.objects.filter(nombre__contains = nombre)

       elif 'btnBuscar' in request.POST:
           item = Producto.objects.get(pk = id)

       elif 'btnEliminar' in request.POST:
            item = Producto.objects.get(pk = id)
            item.delete()
            mensaje = "El regitro " + item.nombre + " fue eliminado con exito!"
            item = {}
            


    contexto = {'mensaje' : mensaje, 'lista' : lista, 'item' : item, 'cmbAnime' : cmbAnime, 'cmbMarca': cmbMarca, 'cmbTipo' : cmbTipo, 'errores' : errores}
    return render(request, 'producto.html', contexto)


def buscarPorId(modelo, pk):
    try:
        objeto = modelo.objects.get(pk = pk)
    except:
        objeto = None
    return objeto




