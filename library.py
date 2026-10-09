books = [
    {
        "title": "I Am Back",
        "author": "Sauu",
        "price": 500
    },
    {
        "title": "You Are Not",
        "author": "Messi",
        "price": 1000
    },
    {
        "title": "Forward",
        "author": "Shein",
        "price": 10000
    }
]

def show_book():
    print('\n___book list___')
    
    for book in books:
        print(
           book['title'],
           '| author:',book['author'],
           '| price:',book['price'],"MMK"
        )
        
def search_book():
    keyword=input("\n Search book:").lower() 
    
    found=False
    
    for book in books:
        if keyword in book['title'].lower():
            print(
                'found:',
                book['title'],
                '| author:',book['author'],
                '| price:',book['price'],"MMK"
            )
        
            found=True
        
    if found==False:
            print('book not found.') 
            
def access_book():
    title=input('\n Enter book title:').lower()   
    
    for book in books:
        if book['title'].lower()==title:
         print('\nAccess granted')
         print('book:',book['title'])
         print('author:',book['author'])
         print('Access: 30 days')
         return
        
    print('book not found') 
        
while True:
    print('\n====DIGITAL LIBRARY====')
    print("1.Showbook")
    print("2.Search book")
    print("3.Access book")
    print("4.Exit")
    
    choice=input('Choose:')
    
    if choice=="1":
        show_book()
        
    elif choice=="2":
        search_book()  
        
    elif choice=="3":
        access_book() 
        
    elif choice=="4":
        print("Goodbye")
        break
        
    else:
        print("invalid choice") 
        
    
           
              
        
    
         
        
            
          