

def my_function():
    import json
    from book_recom_main.models import Book, Rating, User
    with open('Books.json', 'r') as json_file:
        data = json.load(json_file)

    for book_data in data['books']:
        book = Book(book_data)
        book.save()

    for rating_data in data['ratings']:
        rating = Rating(rating_data)
        rating.save()

    for user_data in data['users']:
        user = User(user_data)
        user.save()

if __name__ == "__main__":
    # Call your function when necessary
    my_function()