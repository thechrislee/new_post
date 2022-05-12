#!/usr/bin/env python3

"""
Author: Chris Lee

Purpose: new_post.py is my attempt at using the python standard libary to generate a boilerplate
for jekyll blog posts. Some of the ideas were taken from Ken Youens-Clark's book,
'Tiny Python Project'.
"""

import argparse
import string
from datetime import datetime

# --------------------------------------------------
def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(
        description="Generate blog post file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "filename", metavar="name", type=str, help="the name of the file to write"
    )
    parser.add_argument("title", metavar="title", type=str, help="blog title")
    parser.add_argument(
        "-d", "--dir", metavar="DIR", type=str, default=".", help="output directory"
    )
    parser.add_argument(
        "-c", "--categories", metavar="categories", nargs="+", default="jekyll"
    )
    args = parser.parse_args()
    return args


# --------------------------------------------------
def read_file(path):
    """Read data from file"""
    with open(path) as file:
        data = "".join([line for line in file])
    return data


# --------------------------------------------------
def create_post(args):
    """Generate blog post"""
    template_path = "templates/template.md"
    title = args.title
    categories = " ".join(args.categories)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    ymd = timestamp.split()[0]
    file_name = f"{args.dir}/{ymd}-{args.filename}.md"
    print(f"filname: {file_name}")

    mapping = {"title": title, "timestamp": timestamp, "categories": categories}
    template = string.Template(read_file(template_path))
    data = template.safe_substitute(mapping)

    # write template
    with open(file_name, "w") as file:
        for line in data:
            file.write(line)


# --------------------------------------------------
def main():
    """Get on the good foot..."""
    args = get_args()
    create_post(args)


# --------------------------------------------------

if __name__ == "__main__":
    main()
