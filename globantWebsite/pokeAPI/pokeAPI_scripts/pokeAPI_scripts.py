import requests
import numpy as np
import pylab as pl
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_berries_number(verbose = False):
    """Cuento cuantas berries hay"""

    # Pido la respuesta de la API externa
    response            = requests.get( os.environ["POKEAPI_MAIN_URL"] )

    # Un codigo 200 indica que se obtuvieron datos satisfactoriamente
    try:
        if response.status_code == 200:
            payload     = response.json()
            nberries    = payload.get( 'count', [] )
            
            if verbose == True:
                print('There are {} berries in the dataset'.format( nberries ))
    except:        
        if verbose == True:
            print('ERROR! Something went wrong while loading data')

            nberries    = None

    return nberries

def get_berries_data(nberries, verbose = False):
    """Obtengo los nombres y datos de cada berry"""

    # Obtengo los datos de las berries
    try:
        berry_names      = []
        berry_grow_times = []
        for k in range(nberries+1):
            response = requests.get( os.environ["POKEAPI_MAIN_URL"] + str(k) )
            
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
        berry_names      = None
        berry_grow_times = None
        print('ERROR! Something went wrong while loading data')

    return berry_names, berry_grow_times

def get_json_data(nberries, berri_names, berri_grow_times):    
    # Armo el diccionrio JSON
    json_data = {}
    for k in range(nberries+1):
        json_data[k] = {
            'name' : berri_names[k-1],
            'grow_time' : int(berri_grow_times[k-1]),
        }

    json_object = json.dumps(json_data, indent = 4) 
    #print(json_object)

    return json_object

def plot_berries_hist(berry_grow_times, show = False, savefig = True):
    """Hago un histograma para mostrar los datos""" 

    # Genero el grafico
    pl.figure()
    pl.hist(berry_grow_times)
    pl.grid()
    pl.xlabel('Berry Grow Time')
    pl.ylabel('Ocurrences')
    pl.title("Berries's Grow Times Histogram")
   
    # Guardo la figura
    if savefig == True:
        pl.savefig("./pokeAPI/static/img/berries_hist.png", dpi = 100)

    # Cierro la figura
    if show is True:
        pl.show()
    pl.close()

if __name__ == '__main__':
    nberries = get_berries_number(verbose = True)
    berry_names, berry_grow_times = get_berries_data(nberries, verbose = True)
    plot_berries_hist(berry_grow_times, show = True, savefig = False)