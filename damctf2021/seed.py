#!/usr/bin/env python3
import sys
import time
import random
import hashlib

def seed():
    return round(time.time())

def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def main():
    while True:
        s = 1634187287
        print(s)
        random.seed(s, version=2)

        x = random.random()
        flag = hash(x)
        print(flag)

        if 'b9ff3ebf' in flag:
            with open("./flag", "w") as f:
                f.write(f"dam{{{flag}}}")
            f.close()
            break

        print(f"Incorrect: {x}")
    print("Good job <3")

if __name__ == "__main__":
   sys.exit(main())

##for i in range(1633486367,1636164767):
##        s =i
##        print(i)
##        random.seed(i,version=2)
##        x=random.random()
##        if(x==0.3322089622063289):
##            print(x)
##            break
##        i=+1



