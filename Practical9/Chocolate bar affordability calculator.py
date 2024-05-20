total_money=float(input("please write the money you have: "))
price=float(input("please write the price of one chocolate bar: ")) #get the values
def buy_number(total_money, price) :
    number=int(total_money/price)
    return number   #calculate the number of chocolate
number =buy_number(total_money, price)
print(number)
