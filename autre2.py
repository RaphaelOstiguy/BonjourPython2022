#!/usr/bin/env python3
"""
Autre scripte pour appeler les fonctions
du scripte principale, version 2.

Par: Raphael Ostiguy
   """

from main import bonjour
from main import compter


def main():
    """
    invoque les fonction de main
    """
    bonjour('Ostiguy R.')
    compter(3)


if __name__ == '__main__':
    main()
