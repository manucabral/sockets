require 'socket'
server = TCPServer.new('127.0.0.1', 8888)
puts 'Servidor iniciado en 127.0.0.1:8888'

client = server.accept
while (tmp = client.recv(10) and tmp != 'SALIR')
    puts tmp
    client.puts '>> Recibido'
end