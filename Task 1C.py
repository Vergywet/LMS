books = []
members = []

book = ({'book_id':int(input('Enter the book id :')),
                  'title':input('Enter the book title: '),
                  'author':input('Enter the book author :'),
                  'status':input('Enter the status : '),
    })

books.append(book)

member = ({'member_id':int(input('Enter member id : ')),
                    'name':input('Enter the name : '),
                    'borrowed':[],
                    })
members.append(member)

print("Books :",books)
print("Members : ",members)
