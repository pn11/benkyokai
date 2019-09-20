// Go を初めて書いた。昨日書いた Swift (ABC132/A.swift) よりは分かりやすかったけど、かなり C.
package main
import "fmt"

func main() {
    var a string
    fmt.Scan(&a)
    var ans = "Good"
    for i := 0; i < 3; i++ {
        if a[i] == a[i+1]{
            ans = "Bad"
        }
    }
    fmt.Println(ans)
}
