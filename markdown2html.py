#!/usr/bin/python3
"""Markdown"""

if __name__ == "__main__":
    import os
    from sys import argv, stderr
    
    if len(argv) != 3:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(argv[1]):
        stderr.write(f"Missing {argv[1]}\n")
        exit(1)
    with open(argv[1], "r") as f:
        with open(argv[2], "a") as nw:
            for line in f:
                count_tag = line.count("#")
                if count_tag > 0 and count_tag <= 6:
                    new_l = line.strip("# ")
                    a = new_l.rstrip('\n')
                    nw.write(f"<h{count_tag}>{a}</h{count_tag}> \n")
    print(end="")
    exit(0)
