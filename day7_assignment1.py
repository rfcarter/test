class Company():
    def __init__(self, name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue
    def serve_customer(self, customer_cost):
        self.total_revenue = self.total_revenue - customer_cost
    def gain_employees(self, new_employees):
        self.num_employees = self.num_employees + len(new_employees)

company=Company("MyCo", "Electronic", 100, 130256)
print(company.name, company.industry_type, company.num_employees, company.total_revenue)
company.serve_customer(5000)
company.gain_employees(("Jones", "Smith", "Wilson"))
print(company.name, company.industry_type, company.num_employees, company.total_revenue)