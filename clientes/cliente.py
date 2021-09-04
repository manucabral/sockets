from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror
from sys import argv


def error(mensaje):
    print(mensaje)
    exit(-1)


def verificar_argv():
    if len(argv) < 3:
        error(f'Faltan argumentos, ejemplo: {argv[0]} [HOST] [PUERTO]')


def conectar_socket(socket, direccion):
    try:
        socket.connect(direccion)
    except ConnectionRefusedError:
        error(
            f'No hay un servidor escuchando en {direccion[0]}:{direccion[1]}')


def escuchar(socket):
    nombre_usuario = input('Nombre de usuario: ')
    mensaje = ":D"
    while mensaje != 'SALIR':
        mensaje = input('> ')
        socket.send(f'{nombre_usuario}: {mensaje}'.encode('utf-8'))
        print(socket.recv(128).decode('utf-8'))


def cerrar_conexion(socket):
    socket.close()
    print('Te desconectaste')


def conectar(direccion):
    s = socket(AF_INET, SOCK_STREAM)
    conectar_socket(s, direccion)
    print(f'Conectado al servidor {direccion[0]}:{direccion[1]}')
    escuchar(s)
    cerrar_conexion(s)


def analizar_argv():
    try:
        host = gethostbyname(argv[1])
        puerto = int(argv[2])
    except gaierror:
        error(f'El host "{argv[1]}" es incorrecto')
    except ValueError:
        error(f'Error al analizar el puerto {argv[2]}')
    return host, puerto


def main():
    verificar_argv()
    host, puerto = analizar_argv()
    conectar((host, puerto))


if __name__ == '__main__':
    main()
