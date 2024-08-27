from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def clasificacionPerrito(request):
    cachorro=0
    adulto=0
    senior=0
    try:
        cantidadPerrito = int(input('Ingrese la cantidad de perritos tiene la cosita: '))
        if cantidadPerrito<1:
            raise Exception('error')

        print(cantidadPerrito>0)
        while cantidadPerrito>0:
            cantidad=int(input('ingrese la edad 0 - 16 :'))
            if cantidad >=0 and cantidad <=16:
                if cantidad <= 1:
                    cachorro+=1
                elif cantidad >1 and cantidad <=5:
                    adulto+=1
                elif cantidad > 6:
                    senior+=1
                
                cantidadPerrito=cantidadPerrito-1
            else:
                raise  Exception('error')
    except:
        print('ERROR')       


    html=f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table>
        <tr>
            <th>Calificacion</th>
            <th>Rango de edad</th>
        </tr>
        <tr>
            <td>Cachorros</td>
            <td>{cachorro}</td>
        </tr>
        <tr>
            <td>Adultos</td>
            <td>{adulto}</td>
        </tr>
        <tr>
            <td>senior</td>
            <td>{senior}</td>
        </tr>
    </table>
</body>
</html>"""
    

    return HttpResponse(html)
