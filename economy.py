from enum import Enum
import numpy

''' 
- Economy
The economy class is simply the resprestation of a nations economy. 
[Input] -> [Name and Population]
[Hardcoded Changing Factors] -> [expenses, gdp, average salary]
[Hardcoded Fixed Numbers] -> [interest rates, tax rates]

'''

class SkillLevel(Enum):
    HIGH = 1
    MED = 2
    LOW = 3

class Budget_Type():
    SURPLUS = "surplus"
    DEFICIT = "deficit"

class Taxes:
    def __init__(self, initial_tax_rate):
        self.tax_rates = {
            'income_tax': 0.4,
            'capital_gains': 0.1,
        }
    
    #Getters
    def get_tax_rate(self, tax_type):
        if tax_type in self.tax_rates:
            return self.tax_rates[tax_type]
        else:
            return "Error: Tax type doesn't exist"

    #Setters
    def set_tax_rate(self, new_tax_rate):
        pass

    def increase_tax_rate(self, tax_type, increase_amount):
        pass

class Economy:
    def __init__(self, population, country_name):
        self.government_budget = 0
        self.debt = 0
        self.stability = 0.90
        self.birthrate = 20
        self.budget_type = Budget_Type.SURPLUS
        self.expenses = 100000
        self.interest_rates = 0.05
        self.taxes = Taxes(0.20)
        self.average_salary = 35000

        self.unemployment_rate = 0.01
        self.productivity_rate = 0.10

        #Args
        self.population = population
        self.country_name = country_name    

    # GETTERS
    def get_country_name(self):
        return self.country_name
    
    def get_population(self):
        return str(round(self.population, 0))
    
    def get_government_budget(self):
        return str('{:,}'.format(round(self.government_budget, 3)))

    def get_budget_type(self):
        return self.budget_type
    
    def get_tax_rate(self):
        return self.taxes.get_tax_rate('income_tax')
    
    def get_expenses(self):
        return str(round(self.expenses, 4))
    

    #SETTERS
        
    def calculate_gdp(self):
        # Population * average salary after taxes - expenses.
        gdp = (self.population * (self.average_salary - (self.average_salary * self.tax_rates))) - self.expenses
        return gdp
    
    def calc_government_budget(self):
        #Budget = Population * tax rev - expenses
        self.government_budget = self.population * (self.average_salary * self.tax_rates) - self.expenses
        
        if(self.government_budget > 0):
            self.budget_type = Budget_Type.SURPLUS
        else: 
            self.budget_type = Budget_Type.DEFICIT

        return self.government_budget
    

    def simulate(self):
        if(self.budget_type == Budget_Type.SURPLUS):
            self.interest_rates - 0.005
            self.tax_rates = self.tax_rates - 0.001
            self.expenses = self.expenses + (self.expenses * self.interest_rates)
            self.expenses = self.expenses + (self.expenses * 0.05)
            self.birthrate += self.birthrate * 0.01 
            
        elif(self.budget_type == Budget_Type.DEFICIT):
            self.interest_rates = self.interest_rates + 0.005
            self.tax_rates = self.tax_rates + 0.05

        
        self.population += self.birthrate * self.stability
        
