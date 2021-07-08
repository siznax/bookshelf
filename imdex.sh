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
