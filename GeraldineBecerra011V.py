gas = True
totalPagar = 0
cilindros = True
cantidadCamiones = 0

while gas:
    try:
        nombre = input('Ingrese su nombre: ')
        if len(nombre) < 3:
            print('El nombre debe contener al menos 3 letras')
            continue
        telefono = input('Ingrese su numero telefonico: ')
        if len(telefono) < 8 or len(telefono) > 9 :
            print('El número ingresado debe tener entre 8 a 9 digitos')
            continue
    except ValueError:
        print('Verifica los datos ingresados')
    menu = input(' 1) Compra de camion estandar\n 2) Compra entrega carga especifica\n 3) Imprimir boleta y cerrar pedido\n')
    if menu == '1':
        try:
            cantidadCamiones = int(input('Ingrese la cantidad de camiones que desea \n '))
            if(cantidadCamiones <= 0):
                print(cantidadCamiones)
                print('Debe ingresar un valor mayor a cero') 
            totalKilos = cantidadCamiones * 450
            totalPagar = cantidadCamiones * 765000 
            print(f'Cliente:  {nombre}')
            print(f'Teléfono:  {telefono}')
            print(f'Cantidad de kilos:  {totalKilos}')
            print(f'Camiones:  {cantidadCamiones}')
            print(f'Valor total: {totalPagar} ')  
            otroPedido = input("Desea realizar otro pedido? si/no")
            if otroPedido == 'si':
                gas = True
                totalPagar = 0
                cilindros = True 
                continue
            else:
                gas = False
                totalPagar = 0
                cilindros = False          
        except ValueError:
            print('Debe ingresar un valor mayor a 0')
    elif menu == '2':
        print('Ingrese la cantidad de cilindros')
        while cilindros:
            try:
                cilindros5K = int(input('Ingrese la cantidad de cilindros de 5kg: '))
                total5k = cilindros5K * 5

                cilindros15k = int(input('Ingrese la cantidad de cilindros de 15kg: '))
                total15k = cilindros15k * 15
                
                cilindros45k = int(input('Ingrese la cantidad de cilindros de 45kg: '))
                total45k = cilindros45k * 45 

                totalKilos = total5k + total15k + total45k
                camiones = totalKilos // 450
                if ( camiones %2 == 0):
                    totalEspecifica = camiones * 765000
                else:
                    cantidadCamiones = (totalKilos % 450 ) 
                    print(cantidadCamiones)
                    totalEspecifica = (camiones *765000) +(cantidadCamiones * 1700) + 100000
                    camiones = camiones + 1
                print(f'Cliente:  {nombre}')
                print(f'Teléfono:  {telefono}')
                print(f'Cantidad de kilos:  {totalKilos}')
                print(f'Camiones:  {camiones}')
                print(f'Valor total: ${totalEspecifica} ')                
            except ValueError:
                print('Debes ingresar un numero')
            otroPedido = input("Desea realizar otro pedido? si/no: ")
            if otroPedido.lower() == 'si':
                gas = True
                totalPagar = 0
                cilindros = False    
            else:
                gas = False
                cilindros = False
    elif menu == '3':
        if(totalKilos == 0 ):
            otroPedido = input("Desea realizar otro pedido? si/no: ")
            gas = False
            cilindros = False
print('Gracias por su compra') 


