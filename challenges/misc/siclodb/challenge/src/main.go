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
    nopp = `u think u can heck me 😼❌`
    notvalid = `uh!`
    blacklist  = []string{"get","acl","bf","flush","kill","fcall","save","flag","keydb","exec","auth","merge","debug","help","flushdb","client","set","getrange","mget","exists","dump","del","hset","hget","substr","append","keys","scan"}
)

func isValid(text string) bool {
    return utf8.ValidString(text)
}

func getUserCmd() []string {
    var command []string
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Println("-> Enter an empty line to quit!")
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
                if strings.Contains(strings.ToLower(command), bad) {
                    fmt.Println(nopp)
                    os.Exit(1337)
                }
            }
        }
        command = append(command, user_input)
        break
    }
    return command
}

func execKeydbCli(command []string) {
    for _, command := range command {
        cmd := exec.Command("/usr/bin/keydb-cli")
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