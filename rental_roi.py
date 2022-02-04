class ROI():
    def __init__(self, income = 0, expenses = 0, cash_flow = 0, roi = 0):
        self.income = income 
        self.expenses = expenses 
        self.cash_flow = cash_flow 
        self.roi = roi

    def monthly_Income(self):    
        print("If you dont know the answer to any of these questions please just type 0")
        available_spaces = input("How many tenants can your property hold? ")
        monthly_each = input("How much would each tenant pay monthly for rent alone? For example if rent for one tenant would be $1,000. Type in 1000. No '$' or ',' please ")
        extra = input("Is there any extra fees that you will be charging your tennants? y/n ")
        if extra.lower() == 'y':
            other_charge = input("How much extra would each tenant have to pay not including the rent? For example if extras for one tenant would be $200. Type in 200. No '$' or ',' please ")
            self.income = (int(monthly_each) * int(available_spaces)) + (int(available_spaces) * int(other_charge))
            ROI.monthly_Expenses(self)
        elif extra.lower() == 'n':
            self.income = int(monthly_each) * int(available_spaces)
            ROI.monthly_Expenses(self)
    
    def monthly_Expenses(self):
        vacancy = .05 * self.income
        future_exp = .1 * self.income
        tax_expense = input("How much would the monthly tax be on the property? Again please don't use '$' or ',' ")
        insurance = input("How much is insurance monthly for the property? Again please don't use '$' or ','")
        mortgage = input("What is the approximate mortgage on the proprety? Again please don't use '$' or ','")
        utilities = input("Will you be charging your tenants for utilities? y/n ")
        if utilities.lower() == 'y':
            your_util_cost = 0
        elif utilities.lower() == 'n':
            your_util_cost = input("Estimate the monthly utitliy cost of the entire building. Again please don't use '$' or ',' ")
        manager = input("Will you be managing your own property? y/n ")
        if manager.lower() == 'n':
            manager_cost = .1 * self.income
            self.expenses = int(vacancy) + int(future_exp) + int(tax_expense) + int(insurance) + int(mortgage) + int(your_util_cost) + int(manager_cost)
            ROI.cashFlow(self)
        elif manager.lower() == 'y':
            self.expenses = int(vacancy) + int(future_exp) + int(tax_expense) + int(insurance) + int(mortgage) + int(your_util_cost)
            ROI.cashFlow(self)

    def cashFlow(self):
        monthly_cashflow = self.income - self.expenses
        self.cash_flow = monthly_cashflow * 12
        ROI.cashOnCashROI(self)

    def cashOnCashROI(self):
        down_payment = input("What was your down payment for your property? if $50,000 please just type 50000. Don't use '$' or ',' ")
        closing_cost = input("How much is the closing cost for the property? Again please no '$' or ',' ")
        rehab_bud = input("How much is it going to cost to get it to the point that you can rent it out? Again please no '$', or ',' ")
        other = input("Any other cost that you can think of just input number here. If no other costs just type 0. Please no '$' or ',' ")
        total_investment = int(down_payment) + int(closing_cost) + int(rehab_bud) + int(other)
        self.roi = (self.cash_flow / total_investment) * 100
        newROI = str(self.roi)
        print(f"{newROI[:4]}% ROI")


def runROI():
    my_roi = ROI()
    my_roi.monthly_Income()

runROI()


        
