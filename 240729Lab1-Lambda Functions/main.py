from functools import reduce

def main():
    # ex1
    add_15 = lambda x: x + 15
    print(add_15(10))
    
    # ex2
    multiplies_3 = lambda x: x * 3
    print(multiplies_3(10))

    # ex3
    square = lambda x: x ** 2
    print(square(10))

    # ex4
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

    # ex5
    temperatures = [25, 30, 35, 40, 45]
    fahrenheit_temperatures = list(map(lambda c: (c * 9/5) + 32, temperatures))
    print(fahrenheit_temperatures)

    # ex6
    numbers = [1, 2]
    max_number = max(numbers, key=lambda x: x)
    print(max_number)

    # ex7
    numbers = [1, 2, 3, 4, 5]
    reduce_result = reduce(lambda x, y: x * y, numbers)
    print(reduce_result)

    # ex8
    numbers = [1, 2, 3, 4, 5, 6]
    filtered_numbers = list(filter(lambda x: x % 3 == 0, numbers))
    print(filtered_numbers)

    # ex9
    rectangle_area = lambda length, width: length * width
    print(rectangle_area(5, 10))

    # ex10
    numbers = [1, 2, 3, 4, 5]
    incremented_numbers = list(map(lambda x: x + 1, numbers))
    print(incremented_numbers)

    # ex11
    words = ['apple', 'banana', 'cherry']
    word_lengths = list(map(lambda x: len(x), words))
    print(word_lengths)

    # ex12
    letters = ['A', 'B']
    concatenated_letters = reduce(lambda x, y: x + y, letters)
    print(concatenated_letters)

    # ex13
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    greater_than_5 = list(filter(lambda x: x > 5, numbers))
    print(greater_than_5)

    # ex14
    words = ['apple', 'banana', 'cherry']
    contain_a = list(filter(lambda x: 'a' in x, words))
    print(contain_a)

    # ex15
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print(doubled_numbers)

    # ex16
    words = ['apple', 'banana', 'madam']
    palindrome_words = list(filter(lambda x: x == x[::-1], words))
    print(palindrome_words)

    # ex17
    tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
    tuples.sort(key=lambda x: x[1])
    print(tuples)

    # ex18
    words = ["apple", "bat", "cat", "dolphin"]
    longer_than_3 = list(filter(lambda x: len(x) > 3, words))
    print(longer_than_3)

    # ex19
    numbers = range(1, 11)
    factorial_result = reduce(lambda x, y: x * y, numbers)
    print(factorial_result)

    # ex20
    people = [
        {'name': 'Alice', 'age': 25}, 
        {'name': 'Bob', 'age': 30}, 
        {'name': 'Charlie', 'age': 20}
        ]
    people.sort(key=lambda x: x['age'])
    print(people)

    # ex21
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flattened_list = reduce(lambda x, y: x + y, nested_list)
    print(flattened_list)

    # ex22
    word = "apple"
    count_vowels = len(list(filter(lambda x: x in 'aeiou', word)))
    print(count_vowels)

    # ex23
    numbers = [1, 2, 3, 4, 5]
    second_largest = lambda numbers: sorted(numbers)[-2]
    print(second_largest(numbers))

    # ex24
    numbers = [1, 2, 2, 3, 4, 4, 5]
    remove_duplicates = list(set(numbers))
    print(remove_duplicates)

    # ex25
    words = ["apple", "banana", "cherry", "date"]
    longest_word = max(words, key=lambda x: len(x))
    print(longest_word)

if __name__ == "__main__":
    main()
