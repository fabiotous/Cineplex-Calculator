tax = 0.13
popcorn = int(input("Enter the amount of popcorn"))
price_popcorn = popcorn * 4.29
candy = int(input("Enter the amount of candy"))
price_candy = candy * 3.49
pop = int(input("Enter the amount of pop"))
price_pop = pop * 1.99
SUBTOTAL = price_popcorn + price_candy + price_pop
HST = (price_popcorn * tax) + (price_candy * tax) + (price_pop * tax)
GRANDTOTAL = SUBTOTAL + HST
print ("SUBTOTAL:             $",SUBTOTAL)
print ("HST                    $",HST)
print ("GRANDTOTAL            $",GRANDTOTAL)
AMOUNTTENDERED = int(input("How much do you pay in total with cash"))
CHANGE = AMOUNTTENDERED - GRANDTOTAL
print ("AMOUNTTENDERED         ",AMOUNTTENDERED)
print ("CHANGE                $",CHANGE)


