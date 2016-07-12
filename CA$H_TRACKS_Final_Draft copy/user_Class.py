# CLASS: USER


from month_Class import Month

import csv

from os import listdir



class User(Month):
	def __init__(self, month = None, year = None, income = None, budget = None, expenditures = None, budget_spending_tracker = None, dict_order = None):
		Month.__init__(self, month, year)
		self.my_month = Month(self.month, self.year)

		self.my_month.income = self.income 
		self.my_month.budget = self.budget
		self.my_month.expenditures = self.expenditures
		self.my_month.budget_spending_tracker = self.budget_spending_tracker
		self.dict_order = self.dict_order



	def define_new_month(self, my_month, my_year):
		return Month(self.month, self.year)



## MENU ITEMS ##


	def show_welcome_message(self):
		print "\n"
		print "CA$H TRACKS"
		print "\n"


	def main(self):
		self.show_welcome_message()
		menu = (
			"1. Create Budget",
			"2. View / Edit Budget",
			"3. Add Transaction",
			"4. Track Spending Goals",
			"5. Exit"
				)
		while (True):
			for choice in menu:
				print choice
			user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
			if (user_choice == "5") or (str.upper(user_choice) == "EXIT"): 
				exit()
			
			elif user_choice == "1":
				self.option_create_budget()
			
			elif user_choice == "2":
				self.option_view_edit_budget(self.my_month.month)
			
			elif user_choice == "3":
				self.option_add_transaction(self.my_month.month)
			
			elif user_choice == "4":
				self.option_track_budget_spending_goals(self.my_month.month)
			
			elif  user_choice not in ("1" , "2", "3", "4"):
				print "Woops! Please choose which action by selecting it's cooresponding number."


	def option_create_budget(self):
		menu = (
			"1. Create New Budget",
			"2. Use a Budget from a Previous Month",
			"3. Create Budget from Previous Month's Expenditures",
			"4. Return to Home"
			)
		for choice in menu:
			print "\t" + choice 
		user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
		
		if (user_choice == "4") or (str.upper(user_choice) == "HOME"):  # option 4: return home
			None
		
		elif (user_choice == "1"):      # option 1: Create New Budget
			self.create_new_budget()  


		elif (user_choice == "2"):      # option 2: Use a Budget from a Previous Month
			self.display_month_files()
			
			print "Please be cautious of spelling!"
			month_name = raw_input("Type desired month's budget: ")
			
			print "\n"
			
			self.return_formated_dict(self.extract_budget_data_from_file(month_name.upper()))
			print "\n"
			
			budget_question = raw_input("Would you like to use %s's budget data for this month's budget? (Y/N): " % (self.extract_month(month_name.upper())))
			print "\n"
			
			if (str.upper(budget_question) == "Y"):  # use budget from previous month
				self.my_month.month = (raw_input("Current Month: ").upper())
				self.my_month.year = raw_input("Current Year: ")
				currentMonth = self.define_new_month(self.my_month.month, self.my_month.year)
				
				currentMonth.budget = (self.extract_budget_data_from_file(month_name.upper()))
				self.my_month.budget = currentMonth.budget
				self.file_save(self.my_month.month)


				print "\n"

				print "%s's Income: $%.2f" % (month_name.upper(), self.extract_income_data_from_file(month_name.upper()))
				
				income_question = raw_input("Would you like to use the same income value? (Y/N): ")
				
				if (str.upper(income_question) == "Y"):  # use same income value
					print "\n"
					
					currentMonth.income = float(self.extract_income_data_from_file(month_name.upper()))
					self.my_month.income = currentMonth.income

					self.return_formated_dict(currentMonth.budget)
					print "Income for this month: $%.2f" %  (currentMonth.income)
					print "Unallocated Money: $%.2f" % (self.calculate_unallocated_money(currentMonth.income, currentMonth.budget))

					self.file_save(self.my_month.month)

					# # # OLD DATA # :
					# self.my_month.income = self.extract_income_data_from_file(month_name.upper())
					# self.view_budget(self.my_month.month)
					# self.file_save(self.my_month.month)


				elif (str.upper(income_question) == "N"):  # use new income
					print "\n"
					currentMonth.income = float(raw_input("This month's income: $"))
					self.file_save(self.my_month.month)
					self.my_month.income = currentMonth.income 

					self.return_formated_dict(currentMonth.budget)
					print "Income for this month: $%.2f" %  (currentMonth.income)
					print "Unallocated Money: $%.2f" % (self.calculate_unallocated_money(currentMonth.income, currentMonth.budget))

					self.file_save(self.my_month.month)

					
			else:
				self.main()

		elif (user_choice == "3"):      # option 3: Create Budget from Previous Month's Expenditures
			self.display_month_files()
			print "\n"
			
			print "Please be cautious of spelling!"
			month_name = raw_input("Type desired month's expenditures to create budget: ")
			
			print "\n"
			
			self.return_formated_dict(self.extract_expenditure_data_from_file(month_name.upper()))
			
			budget_question = raw_input("Would you like to use %s's expenditure data for this month's budget? (Y/N): " % (month_name.upper()))
			print "\n"
			
			if (str.upper(budget_question) == "Y"):  # use other month's expenditure data
				self.my_month.month = (raw_input("Current Month: ").upper())
				self.my_month.year = raw_input("Current Year: ")
				currentMonth = self.define_new_month(self.my_month.month, self.my_month.year)

				currentMonth.budget = (self.extract_expenditure_data_from_file(month_name.upper()))
				self.my_month.budget = currentMonth.budget
				self.file_save(self.my_month.month)


				print "\n"
				print "%s's Income: $%.2f" % (month_name.upper(), self.extract_income_data_from_file(month_name.upper()))
				
				income_question = raw_input("Would you like to use the same income value? (Y/N): ")
				
				if (str.upper(income_question) == "Y"):  #use other month's income data
					print "\n"
					currentMonth.income = float(self.extract_income_data_from_file(month_name.upper()))
					self.my_month.income = currentMonth.income

					self.return_formated_dict(currentMonth.budget)
					print "Income for this month: $%.2f" %  (currentMonth.income)
					print "Unallocated Money: $%.2f" % (self.calculate_unallocated_money(currentMonth.income, currentMonth.budget))

					self.file_save(self.my_month.month)

		
				elif (str.upper(income_question) == "N"): # put new income value
					print "\n"
					currentMonth.income = float(raw_input("This month's income: $"))
					self.file_save(self.my_month.month)
					self.my_month.income = currentMonth.income 

					self.return_formated_dict(currentMonth.budget)
					print "Income for this month: $%.2f" %  (currentMonth.income)
					print "Unallocated Money: $%.2f" % (self.calculate_unallocated_money(currentMonth.income, currentMonth.budget))

					self.file_save(self.my_month.month)


			else: 
				self.main()
			
	
		elif  user_choice not in ("1" , "2", "3", "4"):
			print "\n" + "Woops! Please choose which action by selecting it's cooresponding number." + "\n" 




	def option_view_edit_budget(self, month):
		menu = (
			"1. View Budget", 
			"2. Edit Budget",
			"3. Return to Home"
				)
		while (True): 
			for category in menu:
				print "\t" + category
			user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
		
			if (user_choice == "3") or (str.upper(user_choice) == "HOME"):  # option 3: return home
				self.main()
		
			elif user_choice == "1":    # View Current Budget

				print "\n"
				self.display_month_files()
				print "\t"
				print "Please be cautious of spelling!"
				print "\t"
				month_name = (raw_input("Month: ").upper())
				print "\n"
				self.my_month.month = month_name.upper()
				self.my_month.year = self.extract_year(month_name.upper())
				self.my_month.income = self.extract_income_data_from_file(month_name.upper())
				self.my_month.budget = self.extract_budget_data_from_file(month_name.upper())
				self.my_month.expenditures = self.extract_expenditure_data_from_file(month_name.upper())
				self.my_month.budget_spending_tracker = self.extract_tracker_data_from_file(month_name.upper())

				self.show_budget_message(self.extract_month(month_name.upper()), self.extract_year(month_name.upper()))
				self.view_budget(month_name.upper())
				
				print "\n"
				user_choice2 = raw_input("Would you like to edit the above budget?(Y/N) ")
				
				if (str.upper(user_choice2) == "N"):
					self.main()

				elif (str.upper(user_choice2) == "Y"):  # edit budget
					print "\n"
					print "Edit your budget for %s, %s" % (month_name.upper(), self.extract_year(month_name.upper()))
					
					self.my_month.budget = self.extract_budget_data_from_file(month_name.upper())
					self.my_month.income = self.extract_income_data_from_file(month_name.upper())
					self.edit_budget_value_by_number_listing(self.my_month.budget, self.extract_income_data_from_file(month_name.upper()), self.extract_month(month_name.upper()))
					
					self.file_save(month_name.upper())
				

			elif user_choice == "2":    # Edit Current Budget
				
				self.display_month_files()
				print "Please be cautious of spelling!"
				month_name = (raw_input("Month: ").upper())

				self.my_month.month = month_name.upper()
				self.my_month.year = self.extract_year(month_name.upper())
				self.my_month.income = self.extract_income_data_from_file(month_name.upper())
				self.my_month.budget = self.extract_budget_data_from_file(month_name.upper())
				self.my_month.expenditures = self.extract_expenditure_data_from_file(month_name.upper())
				self.my_month.budget_spending_tracker = self.extract_tracker_data_from_file(month_name.upper())
				
				print "Edit your budget for %s, %s" % (month_name.upper(), self.extract_year(month_name.upper()))
		
				self.my_month.budget = self.extract_budget_data_from_file(month_name.upper())
				self.my_month.income = self.extract_income_data_from_file(month_name.upper())
				self.view_budget(self.my_month.month)
				self.file_save(month_name.upper())
				
				
				self.edit_budget_value_by_number_listing(self.extract_budget_data_from_file(month_name.upper()), self.extract_income_data_from_file(month_name.upper()), self.extract_month(month_name.upper()))
				self.file_save(month_name.upper())
			
	


	def option_add_transaction(self, user_month_input = None):

		self.display_month_files()
		print "Please be cautious of spelling!"
		month_name = (raw_input("Month: ").upper())
		self.my_month.month = month_name.upper()
		self.my_month.year = self.extract_year(month_name.upper())
		self.my_month.income = self.extract_income_data_from_file(month_name.upper())
		self.my_month.budget = self.extract_budget_data_from_file(month_name.upper())
		self.my_month.expenditures = self.extract_expenditure_data_from_file(month_name.upper())
		self.my_month.budget_spending_tracker = self.extract_tracker_data_from_file(month_name.upper())

		self.add_transaction_by_number_listing(self.my_month.expenditures, self.my_month.budget_spending_tracker)
		self.file_save(self.my_month.month)
		
	
	def option_track_budget_spending_goals(self, month):

		self.display_month_files()

		print "Please be cautious of spelling!"

		month_name = (raw_input("Month: ").upper())

		self.my_month.month = month_name.upper()
		self.my_month.year = self.extract_year(month_name.upper())
		self.my_month.income = self.extract_income_data_from_file(month_name.upper())
		self.my_month.budget = self.extract_budget_data_from_file(month_name.upper())
		self.my_month.expenditures = self.extract_expenditure_data_from_file(month_name.upper())
		self.my_month.budget_spending_tracker = self.extract_tracker_data_from_file(month_name.upper())


		print "\n"

		self.show_budget_spending_tracker_message(self.my_month.month, self.my_month.year)
		self.calculate_budget_spending_tracker_values(self.my_month.budget, self.my_month.budget_spending_tracker) 
		self.return_formated_budget_spending_tracker(self.my_month.budget_spending_tracker)
		
		self.file_save(self.my_month.month)

		menu = (
			"1. Add Transaction",
			"2. Return home"
				)

		while (True):
			for choice in menu:
				print "\t" + choice
			user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
			
			if (user_choice == "2") or (str.upper(user_choice) == "HOME"):  #option 2: return home
				self.main()
			
			elif user_choice == "1":
				self.option_add_transaction(self.my_month.month)
				
			elif  user_choice not in ("1" , "2"):
				print "Woops! Please choose which action by selecting it's cooresponding number."


	def create_new_budget(self):   # MY_MONTH
		self.my_month.month = raw_input("Current Month: ")
		self.my_month.year = raw_input("Current Year: ")

		self.file_save(self.my_month.month)

		self.show_budget_message(self.my_month.month, self.my_month.year)
		
		self.return_formated_dict(self.my_month.budget)  #prints out entire budget w/ "$0.00" next to each category 

		print "\n"

		self.my_month.set_all_budget_values(self.my_month.budget)

		self.my_month.income = float(raw_input("This month's income: "))
		
		self.file_save(self.my_month.month) 

		print "\n"

		self.show_budget_message(self.my_month.month, self.my_month.year)
		self.view_budget(self.my_month.budget)  #prints budget w/ new values
		
		self.file_save(self.my_month.month)

		self.return_unallocated_money_question()

		self.file_save(self.my_month.month)


	def view_budget(self, my_month):
		self.return_formated_dict(self.my_month.budget)
		self.view_income_message(self.my_month.month)
		print "Unallocated Money: $%.2f" % (self.calculate_unallocated_money(self.my_month.income, self.my_month.budget))

	

	def edit_budget_by_cateogry(self, my_month):
		self.edit_budget_value_by_number_listing(self.my_month.budget, self.my_month.income, self.my_month.month)
		self.file_save(self.my_month.month)


	def add_to_budget(self, budget, unallocated_money):
		self.add_to_budget_by_cateogry_listing(self.my_month.budget, self.my_month.income, self.my_month.month)
		self.file_save(self.my_month.month)


	def return_unallocated_money_question(self): 
		my_month_unallocated_money = float(self.my_month.calculate_unallocated_money(self.my_month.income, self.my_month.calculate_total_est_spending(self.my_month.budget)))
		if my_month_unallocated_money > 0:
			user_choice = raw_input("Based on your monthly income of $%.2f and your total estimated budget of $%.2f, you have $%.2f remaining, would you like to allocate it into budget category? (Y/N) " % (
							self.my_month.income, 
							self.calculate_total_est_spending(self.my_month.budget), #removed self.my_month.calculate_total_est_spending
							my_month_unallocated_money
							))
			if (str.upper(user_choice) == "Y"):  #user wants to add extra money to category 
				#self.add_to_budget(self.my_month.budget, my_month_unallocated_money)
				self.add_to_budget_by_cateogry_listing(self.my_month.budget, self.my_month.income, self.my_month.month)
				self.file_save(self.my_month.month)
			
			elif(str.upper(user_choice) == "N"):
				self.main()

		if my_month_unallocated_money < 0:
			user_choice = raw_input("Your budget of $%.2f is net negative compared with your income of $%.2f.  Would you like to edit your exisitng budget? (Y/N) " % (
							self.calculate_total_est_spending(self.my_month.budget),  #removed self.my_month.calculate_total_est_spending
							self.my_month.income
							))
			if (str.upper(user_choice) == "Y"):  #user wants to add extra money to category 
				#self.edit_budget_by_cateogry(self.my_month.budget)   
				self.edit_budget_value_by_number_listing(self.my_month.budget, self.my_month.income, self.my_month.month)
				self.file_save(self.my_month.month)
			
			else:
				self.main()  


	def show_budget_message(self, my_month, my_year):
		print "Your budget for %s, %s is: " % (my_month.upper(), self.my_month.year)


	def show_budget_spending_tracker_message(self, my_month, my_year):
		print "Budget vs. Spending for %s, %s is: " % (my_month.upper(), self.my_month.year)

	
	def view_income_message(self, my_month):
		print "Income for this month: $%.2f" %  (self.my_month.income)


	def display_month_files(self):
		for file in listdir("/Users/Miranda/Desktop/Intro to Programming/FINAL PROJECT/CA$H_TRACKS_Final_Draft"):
				if file.startswith ("my_month_data_") and file.endswith(".csv"):
					file_name = str(file)
					file_name_split = str(file_name.split("my_month_data_"))
					month = file_name_split[6:-6]
					print month

#### FILE SAVING & WRITING ####

	def file_save(self, month):  #CURRENT ONLY SAVES FOR 1 MONTH - DATA WILL OVERWRITE  (use a file name as a parmameter?)
		with open('my_month_data_' + month + '.csv', 'w') as my_month_out_file:
			fieldnames = [
					'month', 
					'year', 
					'income', 
					'budget_rent',
					'budget_utilities',
					'budget_transportation',
					'budget_food_dining',
					'budget_bars',
					'budget_shopping',
					'budget_personal',
					'budget_health_fitness',
					'budget_entertainment',
					'budget_travel',
					'budget_medical',
					'budget_savings',
					'expenditures_rent',
					'expenditures_utilities',
					'expenditures_transportation',
					'expenditures_food_dining',
					'expenditures_bars',
					'expenditures_shopping',
					'expenditures_personal',
					'expenditures_health_fitness',
					'expenditures_entertainment',
					'expenditures_travel',
					'expenditures_medical',
					'expenditures_savings',
					'budget_spending_tracker_rent',
					'budget_spending_tracker_utilities',
					'budget_spending_tracker_transportation',
					'budget_spending_tracker_food_dining',
					'budget_spending_tracker_bars',
					'budget_spending_tracker_shopping',
					'budget_spending_tracker_personal',
					'budget_spending_tracker_health_fitness',
					'budget_spending_tracker_entertainment',
					'budget_spending_tracker_travel',
					'budget_spending_tracker_medical',
					'budget_spending_tracker_savings'
					]
			writer = csv.DictWriter(my_month_out_file, fieldnames = fieldnames)
			writer.writeheader()
			writer.writerow(
							{
							'month' : self.my_month.month,    #HOW TO INPUT THIS - CALLING %S OF CLASS OBJECT "MONTH"
							'year' : self.my_month.year, 
							'income' : self.my_month.income, #my_month_income, 
							'budget_rent' : self.my_month.budget['Rent'], #my_month_budget_data, 
							'budget_utilities' : self.my_month.budget['Utilities'],
							'budget_transportation' : self.my_month.budget['Transportation'],
							'budget_food_dining' : self.my_month.budget['Food & Dining'],
							'budget_bars' : self.my_month.budget['Bars'],
							'budget_shopping' : self.my_month.budget['Shopping'],
							'budget_personal' : self.my_month.budget['Personal'],
							'budget_health_fitness' : self.my_month.budget['Health & Fitness'],
							'budget_entertainment' : self.my_month.budget['Entertainment'],
							'budget_travel' : self.my_month.budget['Travel'],
							'budget_medical' : self.my_month.budget['Medical'],
							'budget_savings' : self.my_month.budget['Savings'],


							'expenditures_rent' : self.my_month.expenditures['Rent'], #my_month_expenditure_data
							'expenditures_utilities' : self.my_month.expenditures['Utilities'],
							'expenditures_transportation' : self.my_month.expenditures['Transportation'],
							'expenditures_food_dining' : self.my_month.expenditures['Food & Dining'],
							'expenditures_bars' : self.my_month.expenditures['Bars'],
							'expenditures_shopping' : self.my_month.expenditures['Shopping'],
							'expenditures_personal' : self.my_month.expenditures['Personal'],
							'expenditures_health_fitness' : self.my_month.expenditures['Health & Fitness'],
							'expenditures_entertainment' : self.my_month.expenditures['Entertainment'],
							'expenditures_travel' : self.my_month.expenditures['Travel'],
							'expenditures_medical' : self.my_month.expenditures['Medical'],
							'expenditures_savings' : self.my_month.expenditures['Savings'],

							'budget_spending_tracker_rent' : self.my_month.budget_spending_tracker['Rent'], #my_month_budget_spending_tracker_data
							'budget_spending_tracker_utilities' : self.my_month.budget_spending_tracker['Utilities'],
							'budget_spending_tracker_transportation' : self.my_month.budget_spending_tracker['Transportation'],
							'budget_spending_tracker_food_dining' : self.my_month.budget_spending_tracker['Food & Dining'],
							'budget_spending_tracker_bars' : self.my_month.budget_spending_tracker['Bars'],
							'budget_spending_tracker_shopping' : self.my_month.budget_spending_tracker['Shopping'],
							'budget_spending_tracker_personal' : self.my_month.budget_spending_tracker['Personal'],
							'budget_spending_tracker_health_fitness' : self.my_month.budget_spending_tracker['Health & Fitness'],
							'budget_spending_tracker_entertainment' : self.my_month.budget_spending_tracker['Entertainment'],
							'budget_spending_tracker_travel' : self.my_month.budget_spending_tracker['Travel'],
							'budget_spending_tracker_medical' : self.my_month.budget_spending_tracker['Medical'],
							'budget_spending_tracker_savings' : self.my_month.budget_spending_tracker['Savings']
							}
							)

	
	def extract_month(self, month):
		with open('my_month_data_' + month + '.csv') as my_month_in_file:
			reader = csv.DictReader(my_month_in_file)
			for row in reader:
				(row['month'])
									
			extract_month = row['month']
			self.my_month.month = extract_month
			return self.my_month.month

		  
	def extract_year(self, month):
		with open('my_month_data_' + month + '.csv') as my_month_in_file:
			reader = csv.DictReader(my_month_in_file)
			for row in reader:
				(row['year'])
			
			extract_year = row['year']
			self.my_month.year = extract_year
			return self.my_month.year
			

	def extract_income_data_from_file(self, month):
		with open('my_month_data_' + month + '.csv') as my_month_in_file:
			reader = csv.DictReader(my_month_in_file)
			for row in reader:
				(row['income'])
			
			extract_income = float(row['income'])
			self.my_month.income = extract_income
			return self.my_month.income


	def extract_budget_data_from_file(self, month): 
		with open('my_month_data_' + month + '.csv') as my_month_in_file:
			reader = csv.DictReader(my_month_in_file)
			for row in reader:
				(
					row['budget_rent'], 
					row['budget_utilities'], 
					row['budget_transportation'],
					row['budget_food_dining'],
					row['budget_bars'],
					row['budget_shopping'],
					row['budget_personal'],
					row['budget_health_fitness'],
					row['budget_entertainment'],
					row['budget_travel'],
					row['budget_medical'],
					row['budget_savings']
				)
						

			extract_budget_rent = float(row['budget_rent'])
			extract_budget_utilities = float(row['budget_utilities'])
			extract_budget_transportation = float(row['budget_transportation'])
			extract_budget_budget_food_dining = float(row['budget_food_dining'])
			extract_budget_bars = float(row['budget_bars'])
			extract_budget_shopping = float(row['budget_shopping'])
			extract_budget_personal = float(row['budget_personal'])
			extract_budget_health_fitness = float(row['budget_health_fitness'])
			extract_budget_entertainment = float(row['budget_entertainment'])
			extract_budget_travel = float(row['budget_travel'])
			extract_budget_medical = float(row['budget_medical'])
			extract_budget_savings = float(row['budget_savings'])



			self.my_month.budget['Rent'] = extract_budget_rent
			self.my_month.budget['Utilities'] = extract_budget_utilities
			self.my_month.budget['Transportation'] = extract_budget_transportation
			self.my_month.budget['Food & Dining'] = extract_budget_budget_food_dining
			self.my_month.budget['Bars'] = extract_budget_bars
			self.my_month.budget['Shopping'] = extract_budget_shopping
			self.my_month.budget['Personal'] = extract_budget_personal
			self.my_month.budget['Health & Fitnessent'] = extract_budget_health_fitness
			self.my_month.budget['Entertainment'] = extract_budget_entertainment
			self.my_month.budget['Travel'] = extract_budget_travel
			self.my_month.budget['Medical'] = extract_budget_medical
			self.my_month.budget['Savings'] = extract_budget_savings

			return self.my_month.budget


	def extract_expenditure_data_from_file(self, month):  
		with open('my_month_data_' + month + '.csv') as my_month_in_file:
			reader = csv.DictReader(my_month_in_file)
			for row in reader:
				(
					row['expenditures_rent'],
					row['expenditures_utilities'],
					row['expenditures_transportation'],
					row['expenditures_food_dining'],
					row['expenditures_bars'],
					row['expenditures_shopping'],
					row['expenditures_personal'],
					row['expenditures_health_fitness'],
					row['expenditures_entertainment'],
					row['expenditures_travel'],
					row['expenditures_medical'],
					row['expenditures_savings']
				)
						

			extract_expenditures_rent = float(row['expenditures_rent'])
			extract_expenditures_utilities = float(row['expenditures_utilities'])
			extract_expenditures_transportation = float(row['expenditures_transportation'])
			extract_expenditures_food_dining = float(row['expenditures_food_dining'])
			extract_expenditures_bars = float(row['expenditures_bars'])
			extract_expenditures_shopping = float(row['expenditures_shopping'])
			extract_expenditures_personal = float(row['expenditures_personal'])
			extract_expenditures_health_fitness = float(row['expenditures_health_fitness'])
			extract_expenditures_entertainment = float(row['expenditures_entertainment'])
			extract_expenditures_travel = float(row['expenditures_travel'])
			extract_expenditures_medical = float(row['expenditures_medical'])
			extract_expenditures_savings = float(row['expenditures_savings'])



			self.my_month.expenditures['Rent'] = extract_expenditures_rent
			self.my_month.expenditures['Utilities'] = extract_expenditures_utilities
			self.my_month.expenditures['Transportation'] = extract_expenditures_transportation
			self.my_month.expenditures['Food & Dining'] = extract_expenditures_food_dining
			self.my_month.expenditures['Bars'] = extract_expenditures_bars
			self.my_month.expenditures['Shopping'] = extract_expenditures_shopping
			self.my_month.expenditures['Personal'] = extract_expenditures_personal
			self.my_month.expenditures['Health & Fitnessent'] = extract_expenditures_health_fitness
			self.my_month.expenditures['Entertainment'] = extract_expenditures_entertainment
			self.my_month.expenditures['Travel'] = extract_expenditures_travel
			self.my_month.expenditures['Medical'] = extract_expenditures_medical
			self.my_month.expenditures['Savings'] = extract_expenditures_savings

			return self.my_month.expenditures

	
	def extract_tracker_data_from_file(self, month):  
		with open('my_month_data_' +  month + '.csv') as my_month_in_file:
			reader = csv.DictReader(my_month_in_file)
			for row in reader:
				(
					row['budget_spending_tracker_rent'],
					row['budget_spending_tracker_utilities'],
					row['budget_spending_tracker_transportation'],
					row['budget_spending_tracker_food_dining'],
					row['budget_spending_tracker_bars'],
					row['budget_spending_tracker_shopping'],
					row['budget_spending_tracker_personal'],
					row['budget_spending_tracker_health_fitness'],
					row['budget_spending_tracker_entertainment'],
					row['budget_spending_tracker_travel'],
					row['budget_spending_tracker_medical'],
					row['budget_spending_tracker_savings']
				)
						
			
			extract_budget_spending_tracker_rent = float(row['budget_spending_tracker_rent'])
			extract_budget_spending_tracker_utilities = float(row['budget_spending_tracker_utilities'])
			extract_budget_spending_tracker_transportation = float(row['budget_spending_tracker_transportation'])
			extract_budget_spending_tracker_food_dining = float(row['budget_spending_tracker_food_dining'])
			extract_budget_spending_tracker_bars = float(row['budget_spending_tracker_bars'])
			extract_budget_spending_tracker_shopping = float(row['budget_spending_tracker_shopping'])
			extract_budget_spending_tracker_personal = float(row['budget_spending_tracker_personal'])
			extract_budget_spending_tracker_health_fitness = float(row['budget_spending_tracker_health_fitness'])
			extract_budget_spending_tracker_entertainment = float(row['budget_spending_tracker_entertainment'])
			extract_budget_spending_tracker_travel = float(row['budget_spending_tracker_travel'])
			extract_budget_spending_tracker_medical = float(row['budget_spending_tracker_medical'])
			extract_budget_spending_tracker_savings = float(row['budget_spending_tracker_savings'])

			self.my_month.budget_spending_tracker['Rent'] = extract_budget_spending_tracker_rent
			self.my_month.budget_spending_tracker['Utilities'] = extract_budget_spending_tracker_utilities
			self.my_month.budget_spending_tracker['Transportation'] = extract_budget_spending_tracker_transportation
			self.my_month.budget_spending_tracker['Food & Dining'] = extract_budget_spending_tracker_food_dining
			self.my_month.budget_spending_tracker['Bars'] = extract_budget_spending_tracker_bars
			self.my_month.budget_spending_tracker['Shopping'] = extract_budget_spending_tracker_shopping
			self.my_month.budget_spending_tracker['Personal'] = extract_budget_spending_tracker_personal
			self.my_month.budget_spending_tracker['Health & Fitnessent'] = extract_budget_spending_tracker_health_fitness
			self.my_month.budget_spending_tracker['Entertainment'] = extract_budget_spending_tracker_entertainment
			self.my_month.budget_spending_tracker['Travel'] = extract_budget_spending_tracker_travel
			self.my_month.budget_spending_tracker['Medical'] = extract_budget_spending_tracker_medical
			self.my_month.budget_spending_tracker['Savings'] = extract_budget_spending_tracker_savings

			return self.my_month.budget_spending_tracker










