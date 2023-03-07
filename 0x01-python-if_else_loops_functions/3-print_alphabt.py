#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if chr(i) not in 'qe':
        print(f"{chr(i)}", end='')
