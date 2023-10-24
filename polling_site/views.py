from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1>Polls</h1><a href="http://127.0.0.1:8000/admin/">Add New Poll?</a>''')