import requests
import numpy as np
import pylab as pl

POKEAPE__MAIN_URL = 'https://pokeapi.co/api/v2/berry/'

def get_berries_number():
    """Cuento cuantas berries hay"""

    # Pido la respuesta de la API externa
    response            = requests.get( POKEAPE__MAIN_URL )

    # Un codigo 200 indica que se obtuvieron datos satisfactoriamente
    try:
        if response.status_code == 200:
            payload     = response.json()
            nberries    = payload.get( 'count', [] )
            
            print('There is {} berries in the dataset'.format( nberries ))
    except:
        print('ERROR! Something went wrong while loading data')

    return nberries

def get_berries_data(nberries, verbose = True):
    """Obtengo los nombres y datos de cada berry"""

    # Obtengo los datos de las berries
    berry_names      = []
    berry_grow_times = []
    try:
        for k in range(nberries+1):
            response = requests.get( POKEAPE__MAIN_URL + str(k) )
            
            if response.status_code == 200:
                payload             = response.json()
                berry_name          = payload.get( 'name', [] )
                berry_growth_time   = payload.get( 'growth_time', [] )

                if verbose == True:
                    print( 'berry {} ---> {} with grow time of {}'.format(k, berry_name, berry_growth_time) )
                
                # Guardo los datos en listas:
                berry_names.append( berry_name )
                berry_grow_times.append( berry_growth_time )
    except:
        print('ERROR! Something went wrong while loading data')

    return berry_names, berry_grow_times

def plot_berries_hist(berry_grow_times, show = False):
    """Hago un histograma para mostrar los datos""" 

    # Genero el grafico
    pl.figure()
    pl.hist(berry_grow_times)
    pl.grid()
    pl.xlabel('Berri Grow Time')
    pl.ylabel('Ocurrences')
    pl.title("Berri's Grow Times Histogram")
   
    # Guardo la figura
    pl.savefig("./pokeAPI/static/img/berries_hist.png", dpi = 100)

    # Cierro la figura
    if show is True:
        pl.show()
    pl.close()

if __name__ == '__main__':
    nberries = get_berries_number()
    berry_names, berry_grow_times = get_berries_data(nberries)
    plot_berries_hist(berry_grow_times, show = True)