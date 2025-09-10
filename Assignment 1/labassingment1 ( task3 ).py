birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
                      

}



while True:
    print(">>> Welcome to the birthday dictionary")
    print("Type 'exit' to close the program ")
    print("We know the birthdays of: ")
    for names in birthdays:
        print(names)
    
    value = input("Who's birthday you want to look up?")

    if value in birthdays:
        print(f"{value}'s birthday is {birthdays[value]}")

    elif value=="exit":
        break
    else:
        print("The Record for this person is not found in our database")

    
    

    


    
       
   
    
    

    


    
    
