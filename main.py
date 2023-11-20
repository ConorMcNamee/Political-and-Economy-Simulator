from economy import Economy

def main():
    econ = Economy(100, "Utopia")
    turns = 12

    for x in range(1, turns+1):
        econ.calc_government_budget()
        print("Month: "+str(x)+". Welcome to " + econ.get_country_name())
        print("Population: "+ econ.get_population())
        print("Budget: "+ econ.get_government_budget() + ", " + econ.get_budget_type())
        print("Expenses: " + econ.get_expenses())
        print("Tax Rate: " + econ.get_tax_rate())
        print("\n")
        
        econ.simulate()

        

if __name__ == '__main__':
    main()

