# Solution

More than one payload can used to solve the task;
``` 
echo "urlencode(var.SECRET)" | socat - TCP:localhost:13337
echo "title(var.SECRET)" | socat - TCP:localhost:13337
```

**Note** that title() converts the first letter of each word in the given string to uppercase.
https://opentofu.org/docs/language/functions/title/