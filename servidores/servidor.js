const net = require("net");

const server = net
  .createServer((socket) => {
    socket.on("data", (data) => {
      console.log(data.toString());
    });
    socket.write(">> Recibido");
    socket.end("> Cerrando servidor");
  })
  .on("error", (err) => {
    console.error(err);
  });

server.listen(9898, () => {
  console.log("opened server on", server.address().port);
});
