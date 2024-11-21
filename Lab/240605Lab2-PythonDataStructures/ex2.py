from pprint import pprint

def main():
    inventory = {
        "apple": (50, 0.5),
        "banana": (100, 0.2),
        "orange": (75, 0.3),
        "pear": (20, 0.4)
    }

    # 1
    pprint(inventory)

    # 2
    print('\n', sum([v[0]*v[1] for v in inventory.values()]))

    # 3
    inventory['mango'] = (30, 0.6)

    # 4
    inventory['banana'] = (120, 0.2)
    print(inventory, '\n')

    # 5
    del inventory['pear']
    print(inventory)

if __name__ == '__main__':
    main()