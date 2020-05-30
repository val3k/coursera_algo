import sys
from RandomizedQ import RandomizedQueue


def print_random(k, fname):
    rq = RandomizedQueue()
    with open(fname, 'r') as f:
        line = f.readline()
        while line:
            rq.enqueue(line.strip())
            line = f.readline()
    for i in range(k):
        s = rq.sample()
        print(s)


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) != 2:
        sys.exit("Number of strings and filename required")
    else:
        print_random(int(arg[0]), arg[1])