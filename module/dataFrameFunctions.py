"""
FUNCIONES 
"""

"""
Contar los elementos de un DataFrame si es que son valores repetitivos 
"""

def countValuesInSerie(serie, dataInSerie):
    """
    # Description 
        * Contar los elementos de una Serie de pandas si es que son valores repetitivos

    # Parameters
        * serie : dataFrame Object - Toma un dataFrame por parametro  
        * dataInColumn : string - El dato interado

    # Returns
        * la cantidad de iteraciones de un dato 
    """
    return serie[serie == dataInSerie].size
    