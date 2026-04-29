#!/usr/bin/env python3
"""
System Monitor

This script monitors system CPU and memory usage and prints the usage
percentages at regular intervals. Users can specify the interval between
readings and the number of iterations.
"""

import argparse
import psutil
import time


def parse_args():
    parser = argparse.ArgumentParser(description="Monitor CPU and memory usage.")
    parser.add_argument('-i', '--interval', type=float, default=1.0,
                        help='Interval between readings in seconds (default: 1.0)')
    parser.add_argument('-n', '--iterations', type=int, default=5,
                        help='Number of readings to display (0 for infinite)')
    return parser.parse_args()


def main():
    args = parse_args()
    iteration = 0
    while args.iterations == 0 or iteration < args.iterations:
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu:.1f}% | Memory Usage: {mem:.1f}%")
        iteration += 1
        time.sleep(args.interval)


if __name__ == '__main__':
    main()
