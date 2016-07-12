# CLASS:  MONTH


class Month(object):
	def __init__(self, month, year):
		self.month = month
		self.year = year
		self.income = 0.00
		self.budget = {						 # monthly budget
					'Rent' : 0.00,
					'Utilities' : 0.00,
					'Transportation' : 0.00,
					'Food & Dining' : 0.00,
					'Bars' : 0.00,
					'Shopping' : 0.00,
					'Personal' : 0.00,
					'Health & Fitness' : 0.00,
					'Entertainment' : 0.00,
					'Travel' : 0.00,
					'Medical' : 0.00,
					'Savings' :0.00
					}
		self.expenditures = {    			 # monthly expenditures [items user spends money on]
					'Rent' : 0.00,
					'Utilities' : 0.00,
					'Transportation' : 0.00,
					'Food & Dining' : 0.00,
					'Bars' : 0.00,
					'Shopping' : 0.00,
					'Personal' : 0.00,
					'Health & Fitness' : 0.00,
					'Entertainment' : 0.00,
					'Travel' : 0.00,
					'Medical' : 0.00,
					'Savings' :0.00
					}
		self.budget_spending_tracker = {      # keeps track of budget - expenditure for each category item
					'Rent' : 0.00,
					'Utilities' : 0.00,
					'Transportation' : 0.00,
					'Food & Dining' : 0.00,
					'Bars' : 0.00,
					'Shopping' : 0.00,
					'Personal' : 0.00,
					'Health & Fitness' : 0.00,
					'Entertainment' : 0.00,
					'Travel' : 0.00,
					'Medical' : 0.00,
					'Savings' :0.00
					}
		self.dict_order = [  				 # order items will print in on program
				'Rent', 
				'Utilities',
				'Transportation',
				'Food & Dining', 
				'Bars', 
				'Shopping', 
				'Personal', 
				'Health & Fitness',
				'Entertainment',
				'Travel',
				'Medical',
				'Savings'
				]



	def set_budget_value(self, budget_category, budget_category_value):  # set values to budget category 
		self.budget[budget_category] = float(budget_category_value)

	def set_all_budget_values(self, budget_category):
		for budget_category in self.dict_order:
			self.budget[budget_category] = float(raw_input("%s Budget: " % (budget_category)))

	def add_to_budget_value(self, budget_category, unallocated_money):
		self.budget[budget_category] = float(self.budget[budget_category] + unallocated_money)

	def add_transaction(self, expenditure_category, transaction_amt):  # add transactions to track monthly spending
		self.expenditures[expenditure_category] = self.expenditures[expenditure_category] + transaction_amt

	def add_transaction_by_number_listing(self, expenditure_dict, budget_spending_tracker_dict):  #add transactions based on number
		while (True):
			print "\t"
			i = 0
			for i in range(len(self.dict_order)):
				print i+1, self.dict_order[i]
				i +=1
			print "13. Return to Home"
			user_input = int(raw_input("Choose which category you would like to add a transaction to by selecting it's corresponding number: "))
			if user_input not in (1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
				print "Woops! Please choose a category by selecting it's cooresponding number."
			elif user_input == 13:
				break
			else:
				i = self.dict_order[user_input -1 ]
				transaction_amt = float(raw_input("Add to %s: $" % (i)))
				self.expenditures[i] = float(self.expenditures[i] + transaction_amt)
				print "You have spent $%.2f in this month's %s budget" % (self.expenditures[i], i)  #(self.expenditures[i], i)
				self.calculate_budget_spending_tracker_value(i)
			


	
	def edit_budget_value_by_number_listing(self, budget_dict, income, month):
		while (True):
			print "\t"
			i = 0
			for i in range(len(self.dict_order)):
				print i+1, self.dict_order[i]
				i +=1
			print "13. Income"
			print "14. Return to Home"
			user_input = int(raw_input("Choose which budget category to edit by selecting it's corresponding number: "))
			if user_input not in (1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):
				print "Woops! Please choose a category by selecting it's cooresponding number."
			elif (user_input == 14):
				break
			elif (user_input == 13):
				print "Your current income is: $%.2f" % (income)
				income = float(raw_input("New income: $"))
				print "Based on your new income of $%.2f, you have $%.2f remaining in %s's budget." % (income, (self.calculate_unallocated_money(income, self.budget)), month)
			else: 
				i = self.dict_order[user_input -1 ]
				print "Your current budget for %s is: $%.2f" % (i, self.budget[i])
				budget_value = float(raw_input("New %s Budget: $" % (i)))
				self.budget[i] = float(budget_value)
				print "Based on your income of $%.2f, you have $%.2f remaining in %s's budget." % (income, (self.calculate_unallocated_money(income, self.budget)), month)

	def add_to_budget_by_cateogry_listing(self, budget_dict, income, month):
		unallocated_money = self.calculate_unallocated_money(self.income, self.calculate_total_est_spending(self.budget))
		while (unallocated_money>= 0):
			print "\t"
			i = 0
			for i in range(len(self.dict_order)):
				print i+1, self.dict_order[i]
				i +=1
			print "13. Return to Home"
			user_input = int(raw_input("Choose which budget category to edit by selecting it's corresponding number: "))
			if user_input not in (1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
				print "Woops! Please choose a category by selecting it's cooresponding number."
			elif (user_input == 13):
				break
			else: 	
				i = self.dict_order[user_input -1 ]
				print "Your current budget for %s is: $%.2f" % (i, self.budget[i])
				additional_budget_value = float(raw_input("Amt. to add to %s budget: $" % (i)))
				self.budget[i] = float(self.budget[i] + additional_budget_value)
				print "Based on your income of $%.2f, you have $%.2f remaining in %s's budget." % (self.income, self.calculate_unallocated_money(self.income, self.budget), self.month)
		

	def calculate_total_est_spending(self, budget): # add all budget values to calculate expected sepending / estimate that months spending (#calculate_total_budget_allocation)
		budget_added = float(
					self.budget['Rent'] +
					self.budget['Utilities'] +
					self.budget['Transportation'] +
					self.budget['Food & Dining'] +
					self.budget['Bars'] +
					self.budget['Shopping'] +
					self.budget['Personal'] +
					self.budget['Health & Fitness'] +
					self.budget['Entertainment'] +
					self.budget['Travel'] +
					self.budget['Medical'] +
					self.budget['Savings']
					)
		return budget_added
	

	def calculate_unallocated_money(self, income, budget):
		unallocated_money = float(income - self.calculate_total_est_spending(budget))
		return unallocated_money

	def calculate_budget_spending_tracker_values(self, budget_dict, expenditure_dict):  
		for key in self.budget.viewkeys() and self.expenditures.viewkeys():
			self.budget_spending_tracker[key] = float(self.budget[key] - self.expenditures[key])
		return self.budget_spending_tracker


	def calculate_budget_spending_tracker_value(self, category):  
		self.budget_spending_tracker[category] = float(self.budget[category] - self.expenditures[category])
		print "You have $%.2f remaining in %s budget" % (self.budget_spending_tracker[category], category)




	def return_formated_dict(self, dict):
		for i in self.dict_order:
			print i + ":", "$" + "%0.2f" % dict[i]


	def return_formated_budget_spending_tracker(self, budget_spending_tracker_dict):
		#self.budget_spending_tracker[category] = float(self.budget[category] - self.expenditures[category])
		for i in self.dict_order:
			print i + ":", "$" + "%0.2f remaining in %s budget" % (self.budget_spending_tracker[i], i)













