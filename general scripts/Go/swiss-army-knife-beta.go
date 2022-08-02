package main
// notes on unfilmilar imports could be found at: https://pkg.go.dev/github.com/kr/fernet#section-readme
import (
	"fmt"
	"https://github.com/fernet/fernet-go"
)

func main() {
	var answer string
	fmt.Println("1: ubuntu update\n2:ubuntu upgrade\n3:tactical encrypt\n4:decrypt\n5:sudo\n6:arch\n7:Flatpak only\npress any other number to exit")
	fmt.Scanln(&answer)
}
