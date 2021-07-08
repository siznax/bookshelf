bookshelf
=========

Your favorite books, movies, shows, etc. on a digital bookshelf

1. Collect cover images
2. Use "Title (YEAR) note" filename convention
3. Index your collection as HTML or JSON with ``imdex.py``
4. Share your bookshelf on GitHub


imdex
-----

```python
imdex - media indexer

    /books
        The Histories (430 BCE) Herodotus.gif
        War and Peace (1869) Lev Tolstoy.jpg
        Harry Potter and the Sorcerer's Stone (1998) J.K. Rowling.png
    
    $ imdex.py books > index.html
    imdexed (3) images in books
    
    $ head index.html
    <a href="https://google.com/search?q=The Histories">
      <img alt="The Histories (430 BCE) Herodotus"
           title="The Histories (430 BCE) Herodotus"
           src="books/The Histories (430 BCE) Herodotus.jpg"></a>
    
    $ imdex.py books --json > index.json
    imdexed (3) images in books
```


Example
-------

```bash
$ cat imdex.sh
#!/bin/sh -x

./imdex.py books  > _books.html
./imdex.py movies > _movies.html
./imdex.py queue  > _queue.html
./imdex.py shows  > _shows.html
./imdex.py stack  > _stack.html

cat books-head.html  _books.html  > books.html
cat movies-head.html _movies.html > movies.html
cat queue-head.html  _queue.html  > queue.html
cat shows-head.html  _shows.html  > shows.html
cat stack-head.html  _stack.html  > stack.html
```

TinyUrl support
---------------

```json
"shows/Star Trek Picard (2021) tinyurl_AmzStarTrekPicard.jpg": {
    "_": [
        "2021",
        "tinyurl_AmzStarTrekPicard",
        "Star Trek Picard",
        "Star Trek Picard (2021)",
        "Star Trek Picard (2021) tinyurl_AmzStarTrekPicard.jpg",
        "https://tinyurl.com/AmzStarTrekPicard"
    ],
    "alt": "Star Trek Picard (2021)",
    "fname": "Star Trek Picard (2021) tinyurl_AmzStarTrekPicard.jpg",
    "href": "https://tinyurl.com/AmzStarTrekPicard",
    "note": "tinyurl_AmzStarTrekPicard",
    "title": "Star Trek Picard",
    "year": "2021"
}
```

@siznax
