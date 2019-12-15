#!/usr/bin/python3

from . import Question
import string


class Q1_1(Question):
    """String with all unique characters"""
    tests = {
            '': True,
            'a': True,
            'ab': True,
            'aa': False
    }

    def v1(self, s):
        return len(set(s)) == len(s)

    def v2(self, s):
        letters = {c: False for c in string.ascii_letters}
        for c in s:
            if letters[c]:
                return False
            letters[c] = True
        return True

    def v3(self, s):
        for idx1, c1 in enumerate(s):
            for idx2, c2 in enumerate(s):
                if idx1 == idx2:
                    continue
                if c1 == c2:
                    return False
        return True


class Q1_2(Question):
    """Reverse C-style string"""
    tests = {
        '0': '0',
        'a0': 'a0',
        'ab0': 'ba0',
        'abc0': 'cba0',
        'abcd0': 'dcba0'
    }

    def v1(self, s):
        s = list(s)
        for i in range(int(len(s) / 2)):
            tmp = s[len(s) - 2 - i]
            s[len(s) - 2 - i] = s[i]
            s[i] = tmp
        return ''.join(s)


class Q1_3(Question):
    """Remove duplicate characters without additional buffer"""
    tests = {
        '': '',
        'a': 'a',
        'aa': 'a',
        'ab': 'ab',
        'aaa': 'a',
        'abbbc': 'abc',
        'abbb': 'ab',
        'ababab': 'ab'
    }

    def v1(self, s):
        length = len(s)
        i = 0
        while i < length-1:
            j = i+1
            while j < length:
                if s[i] == s[j]:
                    s = s[:j] + s[j+1:]
                    length -= 1
                else:
                    j += 1
            i += 1
        return s


class Q1_4(Question):
    """Anagrams"""
    tests = {
        ('', ''): True,
        ('ab', 'ba'): True,
        ('a', 'ab'): False,
        (' ', ' '): True
    }

    def v1(self, s1, s2):
        return sorted(s1) == sorted(s2)

    def v2(self, s1, s2):
        letters1, letters2 = {}, {}
        for c in s1:
            if c in letters1:
                letters1[c] += 1
            else:
                letters1[c] = 1
        for c in s2:
            if c in letters2:
                letters2[c] += 1
            else:
                letters2[c] = 1
        return letters1 == letters2
