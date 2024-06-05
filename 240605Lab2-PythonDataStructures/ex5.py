def main():
    cities = {
        "New York": 8419000,
        "Los Angeles": 3980000,
        "Chicago": 2716000,
        "Houston": 2328000,
        "Phoenix": 1690000
    }

    # 1
    [print(v) for v in cities.values()]

    # 2
    max = 0
    for n, v in cities.items():
        if v > max:
            max = v
            city = n
    print('\nlargest', city, max, '\n')

    # 3
    min = max
    for n, v in cities.items():
        if v < min:
            min = v
            city = n
    print('smallest', city, min, '\n')

    # 4
    cities['Philadelphia'] = 1700000
    print(cities, '\n')

    # 5
    cities['San Francisco'] = 884000
    print(cities, '\n')
    

if __name__ == '__main__':
    main()