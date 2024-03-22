#Normal List
book_codes = [14,15,16,17,18,19,20]
myBook_codes = []
for b in book_codes:
  if b%2==0:
    print(f"{myBook_codes}")


#List Comprehensions
book_codes = [14,15,16,17,18,19,20]
myBook_codes = [ b for b in book_codes if b%2 != 0]
print(f"{myBook_codes}")
