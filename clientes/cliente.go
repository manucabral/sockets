package main

import "os"
import "net"
import "fmt"
import "bufio"

func main() {

  conn, _ := net.Dial("tcp", "127.0.0.1:8123")
  for {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("> ")
    text, _ := reader.ReadString('\n')
    fmt.Fprintf(conn, text + "\n")
    message, _ := bufio.NewReader(conn).ReadString('\n')
    fmt.Print(">> "+message)
  }
}
