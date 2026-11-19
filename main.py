#!/usr/bin/env python3
"""Entry program for news-image-20261119.

Copies the bundled front-page image to /output/entry.png after
validating it: PNG signature, 1024x1024 dimensions, at most 1 MiB.
No network, no clock, no randomness -- two runs write identical bytes.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET = "/output/entry.png"
LIMIT = 1 << 20


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def validate(path):
    size = os.path.getsize(path)
    if size == 0 or size > LIMIT:
        raise ValueError("entry.png is %d bytes, limit is %d" % (size, LIMIT))
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    w, h = struct.unpack(">II", head[16:24])
    if (w, h) != (1024, 1024):
        raise ValueError("entry.png is %dx%d, expected 1024x1024" % (w, h))


def run():
    validate(SOURCE)
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    if os.path.getsize(TARGET) != os.path.getsize(SOURCE):
        raise ValueError("copied file size differs from source")
    if digest(TARGET) != digest(SOURCE):
        raise ValueError("copied file bytes differ from source")


if __name__ == "__main__":
    try:
        run()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
