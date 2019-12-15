#!/usr/bin/python3


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Question:
    def test(self):
        for i in range(1, 100):
            try:
                f = getattr(self, 'v%d' % i)
            except Exception:
                return

            failed = False
            for k, v in self.__class__.tests.items():
                try:
                    r = f(*k) if type(k) == tuple else f(k)
                    assert r == v
                except AssertionError:
                    failed = True
                    print(bcolors.FAIL + '[FAILED] ' + bcolors.ENDC +
                          '%s v%d : %s -> %s instead of %s' %
                          (self.__class__.__name__, i, k, r, v))

            if not failed:
                print(bcolors.OKGREEN + '[PASSED] ' + bcolors.ENDC +
                      '%s v%d' % (self.__class__.__name__, i))


from . import arraysstrings # noqa: E261
__all__ = ['arraysstrings']
