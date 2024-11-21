def main():
    movies = {
        "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
        "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
        "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
        "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
        "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
    }

    # 1
    [print(v) for v in movies.values()]

    # 2
    max = 0
    for n, v in movies.items():
        if v["rating"] > max:
            max = v["rating"]
            movie = n
    print('\nhighest rated', movie, max, '\n')

    # 3
    movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

    # 4
    movies["Inception"]["rating"] = 9.0
    print(movies, '\n')

    # 5
    del movies["Pulp Fiction"]
    print(movies)


if __name__ == '__main__':
    main()