#!/usr/bin/python3

import inspect
import pkgutil

import crackcodinginterview


def run_tests():
    for _, modname, _ in \
      pkgutil.iter_modules(crackcodinginterview.__path__,
                           'crackcodinginterview.'):
        module = __import__(modname, fromlist="dummy")
        for _, obj in inspect.getmembers(module, inspect.isclass):
            try:
                f = getattr(obj(), 'test')
            except AttributeError:
                continue
            f()


if __name__ == '__main__':
    run_tests()
