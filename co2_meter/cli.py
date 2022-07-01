#!/usr/bin/env python

from __future__ import annotations

from pathlib import Path

import defopt

from .data import Data


def rename(path: Path):
    data = Data.from_file(path)
    data.rename_file(path)


if __name__ == "__main__":
    defopt.run([rename])
