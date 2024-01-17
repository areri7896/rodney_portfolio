from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django_xhtml2pdf.utils import generate_pdf
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.lib import pdfencrypt
from django.contrib.staticfiles import finders


#
# # Create your views here.
# def render_pdf_view(request):
#     template_path = 'templates/docss/cv.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="Rodney_Resume.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)
#
#     # create a pdf
#     enc = pdfencrypt.StandardEncryption("Newbie@01", canPrint=1, canModify=False,
#                                         canCopy=False, canAnnotate=False,
#                                         strength=40)
#     pisa_status = pisa.CreatePDF(
#         html, encrypt=enc, dest=response)
#     # if error then show some funny view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

def myview(response):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('templates/docss/cv.html', file_object=resp)
    return result
