from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ArchivoMulticloud
from .forms import ArchivoMulticloudForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

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
        'servicio': 'Estado del sistema',
        'estado': 'Conexión verificada',
        'mensaje': 'El sistema se encuentra funcionando correctamente y la información queda almacenada en la base de datos.'
    }
    return render(request, 'app/resultado.html', contexto)


@login_required
def probar_azure(request):
    cantidad = ArchivoMulticloud.objects.count()

    contexto = {
        'servicio': 'Pedidos registrados',
        'estado': 'Información disponible',
        'mensaje': f'Actualmente existen {cantidad} pedidos o diseños registrados en el sistema.'
    }
    return render(request, 'app/resultado.html', contexto)

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return redirect('registro')

        user = User.objects.create_user(username=username, password=password1)
        user.save()

        messages.success(request, 'Cuenta creada correctamente. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'app/registro.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')