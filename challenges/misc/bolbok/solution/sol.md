# Solution

As mentioned in the challenge description, we are spawned in a [restricted shell](https://en.wikipedia.org/wiki/Restricted_shell). you can use `echo $0` to verify.

Find the path of the new directory that holds the binaries for our user.

 ```
 echo $PATH
 /usr/bolbok/cmds
 ```

Allowed commands;

```
ls /usr/bolbok/cmds
ls uptime grep top rbash
```

who needs `find` when you have `ls` and `grep` ? 

``` 
ls -Ra / | grep *flag* 
.flag
```

okay, now we know that the flag is a hidden file. how can we get its absolute path? `ls -Ra` already shows us the absolute path for the file but is filtered because of the grep command. use the `-B3` option to show the last 3 lines before `.flag`  

``` 
ls -Ra / | grep *flag* -B3
<path>:
.
..
.flag
```

so we finally got the absolute path for the flag. no cat tac! don't worry you still can display the contents of a file using shell built-ins like `echo` and `read`.

```
echo $(< <path>/.flag)
Securinets{FLAG}
or 
while read line; do echo $line; done < <path>/.flag
Securinets{FLAG}
``` 