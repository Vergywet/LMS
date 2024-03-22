#Normal List
book_codes  = [14,15,16,17,18,19,20]
myBook_codes = []
for b in book_codes:
    myBook_codes.append(b)
    print(f"Book codes :{myBook_codes}")

#List Comprehension
book_codes = [14,15,16,17,18,19,20]
myBook_codes = [b for b in book_codes]
print(f"Book codes are :{myBook_codes}")