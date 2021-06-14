from classAplicacion import Aplicacion
from dolarAPI import valorDolar

if __name__=='__main__':
    dolar=valorDolar() ## SE OBTIENE EL VALOR DEL DOLAR OFICIAL DESDE LA API
    mi__app=Aplicacion(dolar)   #SE INICIALIZA LA APLICACION ENVIANDO EL VALOR DEL DOLAR