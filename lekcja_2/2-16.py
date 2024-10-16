# Igor Zamojski
import re


def swapGVR(line: str) -> str:
    return re.sub(r"(GvR)", "Guido van Rossum", line)


if __name__ == '__main__':
    assert swapGVR("""
    GvR is a Dutch programmer. 
    GvR is the creator of Python!
    """) == """
    Guido van Rossum is a Dutch programmer. 
    Guido van Rossum is the creator of Python!
    """
