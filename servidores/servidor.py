from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror
from sys import argv


def error(mensaje):
    print(mensaje)
    exit(-1)


def verificar_argv():
    if len(argv) < 3:
        error(f'Faltan argumentos, ejemplo: {argv[0]} [HOST] [PUERTO]')


def cerrar_conexion(socket):
    socket.close()
    print('Te desconectaste')


def analizar_argv():
    try:
        host = gethostbyname(argv[1])
        puerto = int(argv[2])
    except gaierror:
        error(f'El host "{argv[1]}" es incorrecto')
    except ValueError:
        error(f'Error al analizar el puerto {argv[2]}')
    return host, puerto


def esperar_conexion(socket):
    socket_cliente, direccion = socket.accept()
    print(f'Nueva conexion: {direccion[0]}:{direccion[1]}')
    return socket_cliente, direccion


def enlazar(socket, direccion):
    try:
        socket.bind(direccion)
        socket.listen(1)
        print(f'Servidor iniciado en {direccion[0]}:{direccion[1]}')
    except ValueError:
        error(f'No se pudo enlazar el servidor')


def escuchar(socket, direccion):
    while True:
        dato = socket.recv(1024).decode("utf-8")
        if dato:
            print(f'> {dato}')
            socket.send('>> Recibido'.encode('utf-8'))
        if dato == "SALIR":
            socket.close()
            break
    return


def iniciar_socket(direccion):
    s = socket(AF_INET, SOCK_STREAM)
    enlazar(s, direccion)
    sc, dc = esperar_conexion(s)
    escuchar(sc, dc)
    s.close()


def main():
    verificar_argv()
    host, puerto = analizar_argv()
    iniciar_socket((host, puerto))


if __name__ == '__main__':
    main()
