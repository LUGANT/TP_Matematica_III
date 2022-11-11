"""
FUNCIONES 
"""

"""
Contar los elementos de un DataFrame si es que son valores repetitivos 
"""
import numpy as np
import pandas as pd

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

def serieFromColumn(df,column):
    """
    # Description 
        * devuelve una seríe de elementos de un dataFrame, tomando su columna

    # Parameters
        * df : dataFrame Object - Toma un dataFrame por parametro
        * column : string - La columna del dataFrame

    # Returns
        * Serie de pandas
    """
    return df[column].value_counts()