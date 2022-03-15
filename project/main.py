import sys

from project import project


def main():
    assert len(sys.argv) == 3
    this = sys.argv[1]
    that = sys.argv[2]
    print(project.this_in_that(this, that))


if "__main__" in __name__:
    main()
