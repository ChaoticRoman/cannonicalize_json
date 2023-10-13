#!/usr/bin/env python3
import sys, json

def load(fn):
    with open(fn) as f:
        return json.load(f)


def compactify(fn):
    j = load(fn)
    with open(fn, "w") as f:
        json.dump(j, f, sort_keys=True, separators=(',', ':'))


if __name__ == "__main__":
    compactify(sys.argv[1])
