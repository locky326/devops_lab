#!/usr/bin/env python3


def viskos(Year):
    return (Year % 4 == 0) and (Year % 400 == 0 or Year % 100 != 0)


if __name__ == "__main__":
    """commented input"""
    # Year = int(input())
    # print(viskos(Year))
