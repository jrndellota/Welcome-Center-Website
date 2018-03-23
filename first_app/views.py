# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt

from first_app.models import Attendance
from first_app.forms import ImageForm

import re
import base64
from PIL import Image
#from pyzbar.pyzbar import decode

# Create your views here.

def index(request):
    form = ImageForm()
    code ='this is the qrcode'

    if request.method == 'POST':
        data = ImageForm(request.POST)
        print(data)
        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        image_data= data.cleaned_data['img']
        image_data = dataUrlPattern.match(image_data).group(2)
        image_data = image_data.encode()
        image_data = base64.b64decode(image_data)
        #image = Image.open(image_data)
        code = decode(image_data).data
        print(code)

    return render(request, 'index.html',{"code":code, "form": form})
