from cgitb import html
import os
from time import timezone
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from applications.catalogos.models import Empleado, Equipo
from .models import Responsiva, Detalle, DetalleBackup


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
        'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path



def reporte_responsivas(request):
    template_path = 'responsivas/print.html'
   

    resp = Responsiva.objects.all()
    context = {
        'obj': resp,
        'request': request, 
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filiname="responsivas.pdf"'
    template = get_template(template_path)
    html = template.render(context)


    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def imprimir_responsiva(request, resp_id):
    template_path = 'responsivas/print_one.html'

    enc = Responsiva.objects.filter(id=resp_id).first()
    if enc:
        det = Detalle.objects.filter(responsiva__id=resp_id)
        #emp = Empleado.objects.filter(id=enc.empleado_id).first()
    else:
        det = {}

    context = {
        'det': det,
        'enc':enc,
        'request':request,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filiname="responsiva.pdf"'
    template = get_template(template_path)
    html = template.render(context)


    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def imprimir_devolucion(request, resp_id):
    template_path = 'responsivas/print_devolucion.html'

    enc = Responsiva.objects.filter(id=resp_id).first()
    if enc:
        det = Detalle.objects.filter(responsiva__id=resp_id)
        #emp = Empleado.objects.filter(id=enc.empleado_id).first()
        detdev = DetalleBackup.objects.filter(responsiva_id = enc.id)
    else:
        det = {}

    context = {
        'det': det,
        'enc':enc,
        'request':request,
        'detdev':detdev,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filiname="devolucion.pdf"'
    template = get_template(template_path)
    html = template.render(context)


    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

