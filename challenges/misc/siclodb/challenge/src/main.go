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
    nopp = `❌❌ Not for you lol ❌❌`
    blacklist  = []string{"get","flag","keydb","set","getrange","mget","exists","dump","del","hset","hget","substr","append","keys","scan"}
)

func isValid(text string) bool {
    return utf8.ValidString(text)
}

func getUserCmd() []string {
    var command []string
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        user_input := scanner.Text()

        if user_input == "" {
            break
        }

        if !isValid(user_input) {
            fmt.Println(nopp)
            os.Exit(1337)
        }

        for _, command := range strings.Fields(user_input) {
            for _, bad := range blacklist {
                if strings.Contains(strings.ToLower(command), bad) {
                    fmt.Println(nopp)
                    os.Exit(1337)
                }
            }
        }
        command = append(command, user_input)
    }
    return command
}

func execKeydbCli(command []string) {
    for _, command := range command {
        cmd := exec.Command("/usr/local/bin/keydb-cli")
        cmd.Stdin = strings.NewReader(command)
        output, err := cmd.CombinedOutput()
        if err != nil {
            fmt.Println("Error executing command:", err)
            os.Exit(1)
        } else {
            fmt.Println(string(output))
        }
    }
}

func main() {
    
    command := getUserCmd()
    execKeydbCli(command)
}