#!/usr/bin/env python3

import argparse
import os
from datetime import datetime

flist = []

cstr = argparse.ArgumentParser()
cstr.add_argument("--version", "-V", action="version",
                  help="version", version='v0.14 (c) Dmitriy Shishkovets,  EPAM, 2020')
cstr.add_argument("--path", type=str, nargs="?", const=1, default='.', help="Specific dir choice")
cstr.add_argument("--lp", action="store_true", help="List files from parent dir")
cstr.add_argument("--lr", action="store_true", help="List files recursively", default=False)
cstr.add_argument("--ext", const=1, nargs="?", help="Filter by extension", default='')
cstr.add_argument("--sd", action="store_true", help="Order files by creation date", default=False)
cstr.add_argument("--sn", action="store_true", help="Order out files by name")
args = cstr.parse_args()

spath = args.path
if args.lp:
    spath = '..'


def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(args.ext):
                if args.sd:
                    info = entry.stat()
                    flist.append(f"{get_date(info.st_mtime)} \t {entry.name}")
                else:
                    flist.append(entry.name)
            elif entry.is_dir() and args.lr:
                list_files(entry.path)


def get_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d')
    return formated_date


list_files(spath)
flist.sort()
for e in flist:
    print(e)
