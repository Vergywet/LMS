import pandas as pd

books = []
members = []

book = ({'book_id':int(input('Enter the book id :')),
                  'title':input('Enter the book title: '),
                  'author':input('Enter the book author :'),
                  'status':input('Enter the status : '),
    })

dfB = pd.DataFrame(books)
                  
member = ({'member_id':int(input('Enter member id : ')),
                    'name':input('Enter the name : '),
                    'borrowed':[],
                    })

dfM  = pd.DataFrame(members)

print("Books Frame : ",dfB)

print("Members Frame : ",dfM)