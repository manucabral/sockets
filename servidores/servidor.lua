require('socket');

puerto = 8080;

servidor = socket.bind('*', puerto);

io.write("> Servidor abierto en el puerto "..puerto.."\n");

con = servidor:accept();

io.write("> Nueva conexion");

while True do
    mensaje = con:receive();
    io.write(mensaje .. "\n");
    io.write("Enviar mensaje: ");
    con:send(io.read() .. "\n");
end 

io.read();
