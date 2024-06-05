def main():
    library = {
        "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
        "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
        "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
    }

    # 1
    [print(v) for v in library.values()]

    # 2
    print('\n', library["978-0-14-028329-7"], '\n')

    # 3
    library["978-1-4028-9462-6"] = {
        "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}

    # 4
    library["978-0-7432-7356-5"]["year"] = 1961
    print(library["978-0-7432-7356-5"], '\n')

    # 5
    del library["978-0-452-28423-4"]
    print(library)


if __name__ == '__main__':
    main()