#include <stdio.h>
#include <winsock.h>

// Winsock library
#pragma comment(lib, "ws2_32.lib")

#define RECEIVE_BUFFER_SIZE 32

void close(SOCKET so)
{
    closesocket(so);
    WSACleanup();
    return;
}

int main(int argc, char *argv[])
{
    SOCKET so;
    WSADATA wsa;
    char *message;
    char *server_ip;
    char buffer[RECEIVE_BUFFER_SIZE];
    unsigned short server_port;
    int bytes_received;
    struct sockaddr_in server;

    if (argc != 3)
    {
        printf("Uso: %s <server_ip> <server_port>\n", argv[0]);
        return 1;
    }

    server_ip = argv[1];
    server_port = atoi(argv[2]);

    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0)
    {
        printf("Error: %d\n", WSAGetLastError());
        return 1;
    }

    printf("Winsock iniciado.\n");

    if ((so = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET)
    {
        printf("Error al crear el socket: %d\n", WSAGetLastError());
        return 1;
    }

    printf("Socket creado.\n");

    memset(&server, 0, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(server_ip);
    server.sin_port = htons(server_port);

    if (connect(so, (struct sockaddr *)&server, sizeof server) < 0)
    {
        printf("Fallo al conectar con el servidor: %ld\n", WSAGetLastError());
        close(so);
        return 1;
    }

    printf("Conectado a %s:%d\n", server_ip, server_port);

    message = "ping";
    if (send(so, message, strlen(message), 0) < 0)
    {
        puts("Fallo al envio de datos.");
        close(so);
        return 1;
    }

    puts("Datos recibidos\n");
    if ((bytes_received = recv(so, buffer, RECEIVE_BUFFER_SIZE - 1, 0)) == SOCKET_ERROR)
    {
        puts("Fallo al recibir datos.");
    }

    buffer[bytes_received] = '\0';
    puts(buffer);

    closesocket(so);
    WSACleanup();
    return 0;
}
