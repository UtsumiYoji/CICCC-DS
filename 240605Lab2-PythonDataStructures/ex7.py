from pprint import pprint

def main():
    countries = {
        "USA": "Washington, D.C.",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "Japan": "Tokyo"
    }

    # 1
    pprint(countries)

    # 2
    print('\n', countries["Germany"], '\n')

    # 3
    countries["Australia"] = "Canberra"
    print(countries, '\n')

    # 4
    countries["USA"] = "New Washington"
    print(countries, '\n')

    # 5
    del countries["France"]
    print(countries)


if __name__ == '__main__':
    main()  
