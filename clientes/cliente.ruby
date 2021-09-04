require 'socket'

sock = TCPSocket.new 'localhost', 8123

while line = sock.gets
  puts line
end

sock.close
