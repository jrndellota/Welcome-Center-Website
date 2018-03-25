# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from first_app.models import Attendance
from first_app.forms import ImageForm

import re
import base64
import zbarlight
from PIL import Image
from io import BytesIO

# Create your views here.


def index(request):
    form = ImageForm()
    code = 'this is the qrcode'

    if request.method == 'POST':
        data = ImageForm(request.POST)
        if data.is_valid():
            dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
            image_data = data.cleaned_data['img']
            image_data = dataUrlPattern.match(image_data).group(2)
            image_data = image_data.encode()
            image_data = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_data))
            code = zbarlight.scan_codes('qrcode', image)
            print(code)
        else:
            print('form is not valid')

    return render(request, 'index.html', {"code": code, "form": form})
