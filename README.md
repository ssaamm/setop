setop
=====

Utility for doing set-like operations on files.

Supported operations:

- intersect
- union
- difference

## Example:
    
a.txt:  
    cat
    mouse
    rabbit

b.txt:  
    moose
    rabbit
    giraffe
    cat

    $ setop intersect a.txt b.txt
    rabbit
    cat

## Requirements
- py.test

## Running the tests

    ln -s setop setop.py # symlink setop.py to setop
    py.test setop.py
