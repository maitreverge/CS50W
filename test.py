from random import randrange
import sys

def prompt_positive(display : str) -> int:

    while True:
        try :
            result = int(input(display))
            assert result > 0
            break
        except EOFError:
            sys.exit(0)
        except:
            continue

    return result

def main():

    level = prompt_positive("Level: ")

    random_nb = randrange(0, level)
    print(random_nb)


if __name__ == "__main__":
    main()
