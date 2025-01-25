class Finance:
    def __init__(self, annual_income, desired_monthly, credit_score, 
                 budget_range, down_payment=None, loan_term=None, monthly_debt=None, trade_in=None):
        self.annual_income = annual_income
        self.desired_monthly = desired_monthly
        self.credit_score = credit_score
        self.budget_range = budget_range
        self.down_payment = down_payment
        self.loan_term = loan_term
        self.monthly_debt = monthly_debt
        self.trade_in = trade_in
        self.DTI = None

    def calc_DTI(self, monthly_debt):
        if self.annual_income > 0:
            monthly_income = self.annual_income/12
            self.DTI = (monthly_debt / monthly_income) * 100
            return self.DTI
        elif self.annual_income == 0:
            self.DTI = -1                                           # -1 value for zero income
            return self.DTI
        else: 
            raise ValueError("Annual income must be $0 or more")
        
    
    # estimated affordable price


    # def repr(self)