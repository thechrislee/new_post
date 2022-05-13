# new_post
Python program that generates Jekyll blog posts. Posts are generated using python template strings. 

```python
$ ./new_post.py -h
usage: new_post.py [-h] [-d DIR] [-c categories [categories ...]] name title

Generate blog post file

positional arguments:
  name                  the name of the file to write
  title                 blog title

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     output directory (default: .)
  -c categories [categories ...], --categories categories [categories ...]
```
