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
    wasted = `WASTED 💀 ...Try again!`
    blacklist  = []string{"|", "'", ";", "$", "\\", "#", "*", "&", "^", "@", "!", "<", ">", "%", ":", ",", "?", "{", "}", "`", "diff", "/dev/null", "patch", "./", "alias", "push",  "base64encode","strrev", "format", "file"}
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
            fmt.Println(wasted)
            os.Exit(1337)
        }

        for _, command := range strings.Fields(user_input) {
            for _, bad := range blacklist {
                if strings.Contains(command, bad) {
                    fmt.Println(wasted)
                    os.Exit(1337)
                }
            }
        }
        command = append(command, user_input)

        if len(command) > 1 {
            fmt.Println(wasted)
            os.Exit(1337)
        }
    }
    return command
}

func execTofuConsole(command []string) {
    for _, command := range command {
        cmd := exec.Command("tofu", "console")
        cmd.Stdin = strings.NewReader(command)
        output, err := cmd.CombinedOutput()
        if err != nil {
            fmt.Println("Error executing command:", err)
            os.Exit(1)
        }
        if strings.Contains(string(output), "Securinets{aLl_7h3_wAYS_l3Ad5_70_0n3_s3CR37}") {
            fmt.Println(wasted)
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