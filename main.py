from generators import *
import random


def main():
    list_gens: list[ItemFabric] = [GoldGen(), JamGen(), BricksGen(), ChipGen()]
    for _ in range(10):
        gen = list_gens[random.randint(0, len(list_gens) - 1)].create_item()
        gen.open()


if __name__ == '__main__':
    main()
