import requests

def valorDolar():
    url='https://www.dolarsi.com/api/api.php?type=dolar'
    response=requests.get(url)
    if response.status_code==200:
        response_json=response.json()
        dolar=response_json[0]['casa']['venta']
    return(float(dolar.replace(',','.')))   #SE REEMPLAZA LA COMA POR EL PUNTO PARA PODER CONVERTIRLO EN FLOTANTE