#!/usr/bin/env python3
import sys, json

def load(fn):
    with open(fn) as f:
        return json.load(f)


def canonicalize_json(fn):
    j = load(fn)
    with open(fn, "w") as f:
        json.dump(j, f, sort_keys=True, indent=4)


if __name__ == "__main__":
    canonicalize_json(sys.argv[1])
