from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'fathonidf',
        'role': 'Mage',
        'level': '1'
    }

    return render(request, "main.html", context)