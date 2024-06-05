def main():
    employees = [
        ("John Doe", "Accounting", "john.doe@example.com"),
        ("Jane Smith", "Marketing", "jane.smith@example.com"),
        ("Emily Davis", "HR", "emily.davis@example.com"),
        ("Michael Brown", "IT", "michael.brown@example.com")
    ]

    # 1
    print(employees, '\n')

    # 2
    emails = [d[2] for d in employees]
    emails.sort()
    print(emails, '\n')

    # 3
    employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
    print(employees, '\n')

    # 4
    print([d[1] for d in employees if d[0] == "Jane Smith"][0])


if __name__ == '__main__':
    main()