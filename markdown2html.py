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
            line_count = 0
            ord_line_c = 0
            for line in f:
                if line.startswith("#") is True:
                    count_tag = line.count("#")
                    if count_tag > 0 and count_tag <= 6:
                        if line_count > 0:
                            nw.write("</ul>\n")
                        if ord_line_c > 0:
                            nw.write("</ol>\n")
                        new_l = line.strip("# ")
                        a = new_l.rstrip('\n')
                        nw.write(f"<h{count_tag}>{a}</h{count_tag}> \n")
                        line_count = 0
                        ord_line_c = 0
                if line.startswith("-") is True:
                    if line_count == 0:
                        nw.write("<ul>\n")
                    list_el = line.strip("- ")
                    n_list_el = list_el.rstrip('\n')
                    nw.write(f"<li>{n_list_el}</li>\n")
                    line_count += 1
                if line.startswith("*") is True:
                    if ord_line_c == 0:
                        nw.write("<ol>\n")
                    ord_li = line.strip("* ")
                    n_ord_li = ord_li.rstrip('\n')
                    nw.write(f"<li>{n_ord_li}</li>\n")
                    ord_line_c += 1
            if ord_line_c > 0:
                nw.write("</ol>\n")
            if line_count > 0:
                nw.write("</ul>\n")

    print(end="")
    exit(0)
