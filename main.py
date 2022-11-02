#!/usr/bin/env python3

import time


def bonjour(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bonjour, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def compter(nb, sec=0.25):
    print(f"Je sais compter jusqu'à {nb}:",
          end=' ', flush=True)
    for i in range(1, nb + 1):
        time.sleep(sec)
        print(i, end=' ', flush=True)
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bonjour('Raphael Ostiguy')
    compter(8)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
