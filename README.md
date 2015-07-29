setop
=====

Utility for doing set-like operations on files.

Supported operations:

- intersect
- union
- difference

## Installing

Assuming ~/bin is in your `$PATH`, simply:

    cp setop.py ~/bin/setop
    chmod +x ~/bin/setop

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

If you want to run the tests, you'll need py.test. Otherwise, you're good to go!

## Running the tests

    py.test setop.py
