import sys

from copydirectory import copy_directory
from generatepage import generate_pages_recursive


def main():
    basepath = "/" if len(sys.argv) < 2 else sys.argv[1]
    print(basepath)
    
    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()