#!/usr/bin/env python3
from myapplicationname.nestedlogic.anotherfile import more_logic
from myapplicationname.somelogic import mylogicmethod

if __name__ == '__main__':
    print('this is the entrypoint entrypoint')
    a = mylogicmethod(3)
    more_logic()
