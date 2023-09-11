from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Adventurer\'s Inventory',
        'name': 'Daffa Mohamad Fathoni',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)