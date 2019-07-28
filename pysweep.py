#!/usr/bin/env python

import subprocess
from subprocess import PIPE, STDOUT
import time

def main():
    start = time.time()
    ip_target = '192.168.200.{}'
    ip_alive = []

    for ip in range(1, 256):
        results = subprocess.run(["fping", "-a", "-C 5", "-q", ip_target.format(ip)], stdout=PIPE, stderr=STDOUT, encoding="utf-8")
        if (results.returncode == 0):
            ip_alive.append(results.args[4])

            res_time = results.stdout.split(": ")[1].split("\n")[0]
            print("Host: " + results.args[4] + " is detected online. Response time(s) were: " + res_time)
       
    print("\nThe following hosts were found to be online and responding to ping requests:\n \nDetected Hosts:\n===============")
    for ip in ip_alive:
        print(ip)
    print("\nTotal time to scan took: " + str((time.time() - start) * 1000) + "ms")

if __name__ == '__main__':
    main()