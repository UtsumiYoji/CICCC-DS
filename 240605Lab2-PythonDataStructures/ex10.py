def main():
    members = [
        {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
        {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
        {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
        {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
    ]

    # 1
    [print(v["name"], v["age"]) for v in members]

    # 2
    print('\n', [d["books_borrowed"] for d in members if d["name"] == "Charlie"][0], '\n')

    # 3
    members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})

    # 4
    members[1]["age"] = 31
    print(members, '\n')

    # 5
    del members[3]
    print(members)


if __name__ == '__main__':
    main()