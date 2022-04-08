from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <h3>Holy shit it finally worked</h3>
            <p>The current time is { now }.</p>
            <h6>Copyright by Enairu Eire</h6>
        </body>
    </html>
    '''
    return HttpResponse(html)
