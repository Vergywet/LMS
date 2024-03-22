books = []
members = []

def add_book(book_id, title, author, status):
    books.append({'book_id': book_id, 'title': title, 'author': author, 'status': status})

def add_member(member_id, name):
    members.append({'member_id': member_id, 'name': name})

add_book(2024001, "Python Programming", "Jacob Zuma", "Available")
add_member(1, "Anelisa Maleka")

print("Books : ",books)
print("Members : ",members)
