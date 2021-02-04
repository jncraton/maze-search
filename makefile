all: test

test: 
	python3 -m doctest search.py
