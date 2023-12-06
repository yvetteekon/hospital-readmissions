import sys

from hospital_readmissions.hospital_readmissions import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
