#!/usr/bin/python3

import string


class Q1_1:
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


class Q1_2:
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


class Q1_3:
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


class Q1_4:
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


class Q1_5:
    """Replace spaces by %20"""
    tests = {
        '': '',
        ' ': '%20',
        'a ': 'a%20',
        ' a': '%20a',
        'a b': 'a%20b',
        '  ': '%20%20'
    }

    def v1(self, s):
        return s.replace(' ', '%20')

    def v2(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)


class Q1_6:
    """Rotate image by 90 degrees"""
    tests = {
        (((1, 2), (3, 4)), 2): [[2, 4], [1, 3]],
        (((1, 2, 3), (4, 5, 6), (7, 8, 9)), 3):
        [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    }

    def v1(self, matrix, n):
        return [[row[i] for row in matrix] for i in range(n-1, -1, -1)]


class Q1_7:
    """Set column and row to 0 if matrix element equals 0"""
    tests = {
        (((0, 1), (2, 3)),): [[0, 0], [0, 3]],
        (((1, 2, 0), (4, 5, 6)),): [[0, 0, 0], [4, 5, 0]]
    }

    def v1(self, matrix):
        matrix = [list(row) for row in matrix]

        zeroed = set()
        for idxrow, row in enumerate(matrix):
            for idxcol, col in enumerate(row):
                if col == 0 and (idxrow, idxcol) not in zeroed:
                    for i in range(len(row)):
                        row[i] = 0
                    for i in range(idxrow+1, len(matrix)):
                        if matrix[i][idxcol] != 0:
                            zeroed.add((i, idxcol))
                        matrix[i][idxcol] = 0
                    break
        return matrix

    def v2(self, matrix):
        matrix = [list(row) for row in matrix]

        rows = [0 for _ in range(len(matrix))]
        cols = [0 for _ in range(len(matrix[0]))]
        for idxrow, row in enumerate(matrix):
            for idxcol, col in enumerate(row):
                if col == 0:
                    rows[idxrow] = 1
                    cols[idxcol] = 1

        for idxrow, row in enumerate(matrix):
            for idxcol, col in enumerate(row):
                if rows[idxrow] == 1 or cols[idxcol] == 1:
                    row[idxcol] = 0

        return matrix


class Q1_8:
    """String rotation"""
    tests = {
        ("waterbottle", "erbottlewat"): True,
        ("ab", "ba"): True,
        ("abc", "bac"): False
    }

    def v1(self, s1, s2):
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False

        return s1 in s2 * 2
