Lookup

```sql
CREATE INDEX name_index ON passengers (last);
```

For faster replies if, for example, we quite often lookup passengers for faster replies.

## SQL Injections

Image a form
LOGIN :
PASSWORD :

And when the user plugs a value
```sql
SELECT * FROM users
WHERE username = 'harry' AND password = '12345'
```

So far so good.

Now image that an hacker type in :
LOGIN : hacker"--
PASSWORD :

The internal SQL would be :
```sql
SELECT * FROM users
WHERE username = "hacker"--" AND password = '12345'
```

