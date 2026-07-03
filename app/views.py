from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ArchivoMulticloud
from .forms import ArchivoMulticloudForm


def inicio(request):
    return render(request, 'app/inicio.html')


@login_required
def panel(request):
    return render(request, 'app/panel.html')


@login_required
def archivos(request):
    if request.method == 'POST':
        form = ArchivoMulticloudForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('archivos')
    else:
        form = ArchivoMulticloudForm()

    lista_archivos = ArchivoMulticloud.objects.all().order_by('-fecha_subida')

    return render(request, 'app/archivos.html', {
        'form': form,
        'archivos': lista_archivos
    })


@login_required
def eliminar_archivo(request, archivo_id):
    archivo = get_object_or_404(ArchivoMulticloud, id=archivo_id)

    if request.method == 'POST':
        archivo.archivo.delete(save=False)
        archivo.delete()
        return redirect('archivos')

    return redirect('archivos')


@login_required
def probar_oci(request):
    contexto = {
        'servicio': 'OCI Autonomous Database',
        'estado': 'Pendiente de conexión',
        'mensaje': 'Esta sección se usará para validar la conexión con la base de datos en Oracle Cloud.'
    }
    return render(request, 'app/resultado.html', contexto)


@login_required
def probar_azure(request):
    cantidad = ArchivoMulticloud.objects.count()

    contexto = {
        'servicio': 'Azure Blob Storage',
        'estado': 'Configurado en la aplicación',
        'mensaje': f'La aplicación está preparada para subir archivos a Azure Blob Storage. Archivos registrados: {cantidad}.'
    }
    return render(request, 'app/resultado.html', contexto)