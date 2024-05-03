package main

import (
    "bufio"
    "fmt"
    "os"
    "os/exec"
    "strings"
    "unicode/utf8"
)

var (
    nope = `sry, but i can't simply show my secrets in plaintext. 🔐🙄`
    heck = `Uh! uh! r u trynna heck me 👀? ❌❌`
    notvalid = `soz, can't understand this 😶`
    blacklist  = []string{"$", ":", ",", "#", "?", "{", "}", "`", "abspath", "title", "diff", "patch", "./" , "push", "base64encode","strrev", "format", "file"}
)

func isValid(text string) bool {
    return utf8.ValidString(text)
}

func getUserCmd() []string {
    var command []string
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Println("Enter an empty line to quit!")
    for scanner.Scan() {
        user_input := scanner.Text()

        if user_input == "" {
            break
        }

        if !isValid(user_input) {
            fmt.Println(notvalid)
            os.Exit(1337)
        }

        for _, command := range strings.Fields(user_input) {
            for _, bad := range blacklist {
                if strings.Contains(command, bad) {
                    fmt.Println(heck)
                    os.Exit(1337)
                }
            }
        }
        command = append(command, user_input)
    }
    return command
}

func execTofuConsole(command []string) {
    for _, command := range command {
        cmd := exec.Command("tofu","console")
        cmd.Stdin = strings.NewReader(command)
        output, err := cmd.CombinedOutput()
        if err != nil {
            fmt.Println("Error executing command:", err)
            fmt.Println("Error executing command:", string(output))
            os.Exit(1)
        }
        if strings.Contains(string(output), "83;101;99;117;114;105;110;101;116;115;123;111;80;51;78;55;79;102;85;95;73;53;95;52;119;51;53;79;109;51;95;56;85;55;95;56;51;99;52;82;51;70;117;76;95;87;72;51;110;95;87;79;82;107;105;110;57;95;87;105;55;104;95;53;51;67;114;51;84;115;125") {
            fmt.Println(nope)
            os.Exit(1337)
        } else {
            fmt.Println(string(output))
        }
    }
}

func main() {
    
    command := getUserCmd()
    execTofuConsole(command)
}