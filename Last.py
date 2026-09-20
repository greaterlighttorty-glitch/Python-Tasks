name = input("Enter you name: ")
another_product = "yes"
quantity = 0
amount = 0.0
total_amount = 0.0





while another_product != "no":
    product_name = input('Enter product name: ')
    quantity = int(input(f'Enter quatity of {product_name}: '))
    amount = float(input(f'Enter amount of {product_name}: '))
    another_product = input('Do you wantto add another product? Yes/No: ').lower()

 
    bill = quantity * amount
    total_amount += bill



    if(another_product == "no"):
       print(f" your total bill is ${total_amount:.2f}")
    
