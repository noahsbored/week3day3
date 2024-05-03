class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expense = 0

  
    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        self.__category_name = category_name

  
    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget >= 0:
            self.__allocated_budget = allocated_budget
        else:
            print(" error. should be a positive number.")

    
    def add_expense(self, amount):
        if amount >= 0:
            self.__expense += amount
        else:
            print("error. should be positve.")

  
    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expense
        print("category name:", self.__category_name)
        print("allocated budget:", self.__allocated_budget)
        print("Expenses:", self.__expense)
        print("remaining Budgeb:", remaining_budget)



food_category = BudgetCategory("Food", 10000)
food_category.add_expense(100)
food_category.display_category_summary()
