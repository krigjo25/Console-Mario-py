# Mario Blocks
#   Repositories
import random as r

def main():
    while True:
        n = int(input("Height: "))
        
        mario_v1(n)

        mario_v2(n)


def mario_v2(n):

    #   Counting rows
    for i in range(n):

        # Counting spaces on the left side
        for j in range(n, i + 1, -1):
            print(" ", end="")

        #   Counting Hashes on the left side
        for j in range(i + 1):
            print("#", end="")

        #   Counting spaces in the middle
        print("  ", end="")

        #   Counting Hashes on the right side
        for j in range(i + 1):
            print("#", end="")
        
        print()

    return

def mario_v1(n):

    #   Counting rows
    for i in range(n):


        # Counting spaces on the left side
        for j in range(n, i + 1, -1):
            print(" ", end="")

        #   Counting Hashes on the left side
        for j in range(i + 1):
            print("#", end="")

        print()

    #   Decrease by one
    n -= 1

    return

if __name__ == "__main__":
    main()
