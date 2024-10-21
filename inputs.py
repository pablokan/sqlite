def inputInt(mensaje, mini=-10**38, maxi=10**38) -> int:
    if mini != -10**38 and maxi != 10**38:
        agregarAlMensaje = f' entre {mini} y {maxi}'
    elif mini != -10**38:
        agregarAlMensaje = f' mayor o igual que {mini}'
    elif maxi != 10**38:
        agregarAlMensaje = f' menor o igual que {maxi}'
    else:
        agregarAlMensaje = ""
    mensaje += agregarAlMensaje + ': '
    validado = False
    while not validado:
        s = input(mensaje)
        try:
            n = int(s)
            if mini <= n <= maxi:
                validado = True
        except:
            print('Debe ingresar un entero')
    return n

def inputChoice(opciones, mensaje='Elija una opción'):
    opciones = opciones.split('/')
    mensaje += f' {opciones}: '
    respuesta = ''
    while respuesta not in opciones:
        respuesta = input(mensaje)
    return respuesta

def inputChoiceMenu(opciones, mensaje='Elija una opción'):
    """
    Params: 
    - Ejemplo de opciones: Uno/Dos/Tres
    """
    opciones = opciones.split('/')
    for i in range(len(opciones)):
        print(f'{i+1}) {opciones[i]}')
    print('0) Salir')
    opc = inputInt(mensaje, 0, len(opciones))
    return opciones[opc-1]
