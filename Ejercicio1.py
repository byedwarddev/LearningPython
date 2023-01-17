'''
Pregunta 1 ----------------------------------------------------------------------------------------------------
Se requiere un programa que, dado un dataset con una columna (dataset.csv), construya un dataset con n columnas 
(pedir al usuario el ingreso de este número, no es necesario una validación). En la primera columna se tendrán 
los valores originales del dataset. En la segunda columna se tendrán todos los valores del dataset original, 
excepto el primer valor. En la tercera, todos los elementos, menos los dos primeros, números. Usar la misma lógica 
para las siguientes columnas.
Luego de construido el dataset, mostrar un gráfico de líneas con n subplots. En cada subplot se deberán mostrar los 
valores correspondientes a las distintas columnas.

Pregunta 2 ----------------------------------------------------------------------------------------------------
Se requiere un programa que pida datos de entrada al usuario. Los datos a pedir se pueden apreciar en el siguiente diccionario:
datos = {
    {
        "fecha": "01/01/2020",  # estructura de fecha 
        "id": 15,  # valor entero mayor a 0
        "lecturas": [10, 10.4, 33]  # 3 valores flotantes
    }    
    # pueden haber más registros en el diccionario
}
El número de elementos del diccionario lo decide el usuario que lo ingresa. El programa deberá validar los distintos elementos 
(ver comentarios en el diccionario). Si un dato fue mal ingresado, volver a pedirlo hasta que sea correcto. Luego del ingreso, 
el programa mostrará los 3 id ingresados cuya sumatoria de lecturas sea la mayor.
'''
datos = {
    {
        "fecha": "01/01/2020",  # estructura de fecha 
        "id": 15,  # valor entero mayor a 0
        "lecturas": [10, 10.4, 33]  # 3 valores flotantes
    }    
    # pueden haber más registros en el diccionario
}