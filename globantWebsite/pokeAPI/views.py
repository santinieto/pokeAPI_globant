from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # Basic HTTP response
    # return HttpResponse("""
    # <h1>Index page</h1>
    # """)

    # Render response
    return render(request, 'index.html', {
        'title' : 'Pagina principal - pokeAPI',
    })

def allBerryStats(request):

    return render(request, 'all_berry_stats.html', {
        'title' : 'Estadísticas de las berries',
    })