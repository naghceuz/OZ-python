def cheese_and_cracker(cheese_count, boxes_of_crackers):
	print "You have %d cheese !" % cheese_count
	print "You have %d boxes of crackers !" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"


print "We can just give the function numbers direactly:"
cheese_and_cracker(20,30)

# declare two variables 
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# cheese_and_cracker with variable 
cheese_and_cracker(amount_of_cheese,amount_of_crackers)

#call the function cheese_and_cracker
print "We can even do math inside too:"
cheese_and_cracker(10+20 , 5+6)

# call the function cheese_and_cracker

print "And we can combine the two, variables and math:"
cheese_and_cracker(amount_of_cheese + 100, amount_of_crackers +1000)
