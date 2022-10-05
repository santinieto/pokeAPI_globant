from django.shortcuts import render, HttpResponse
from .pokeAPI_scripts.pokeAPI_scripts import *
import numpy as np

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

    # Obtengo los datos de las berries
    nberries = 5 # get_berries_number()
    berry_names, berry_grow_times = get_berries_data(nberries)

    # Convierto los valores de crecimiento en un arreglo de numpy
    berry_grow_times = np.asarray( berry_grow_times )

    # Creo el diccionario con la informacion
    unique, counts = np.unique(berry_grow_times, return_counts=True)
    frequency = list(zip(unique, counts))

    berries_dicc = {
        #"berries_names": berry_names,
        "min_growth_time": str( min( berry_grow_times ) ),
        "median_growth_time": str( np.median( berry_grow_times ) ),
        "max_growth_time": str( max( berry_grow_times ) ),
        "variance_growth_time": str( np.var( berry_grow_times ) ),
        "mean_growth_time": str( np.mean( berry_grow_times ) ),
        "frequency_growth_time": str( frequency )
    }

    # Genero el grafico
    plot_berries_hist(berry_grow_times)

    # Hago el render
    return render(request, 'all_berry_stats.html', {
        'title' : 'Estadísticas de las berries',
        'nberries' : nberries,
        'berry_names' : berry_names,
        'berry_grow_times' : berry_grow_times,
        'berries_dicc' : berries_dicc,
    })