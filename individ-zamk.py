#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outside(q, r):
    def inside(l):
        s = l.replace(q,r)

        return s
    return inside(l)


if __name__ == '__main__':
    l = "папа"
    a = "п"
    b = "е"
    print(outside(a, b),(l))
