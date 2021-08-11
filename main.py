import random


class EmployeeWage:
    is_full_time = 1
    is_part_time = 2
    wage_per_hour = 20
    maximum_working_days = 20
    maximum_working_hrs = 100

    def get_emp_hrs(self):

        attendance = random.randint(0, 2)
        if attendance == self.is_full_time:
            emp_hrs = 8
        elif attendance == self.is_part_time:
            emp_hrs = 4
        else:
            emp_hrs = 0
        return emp_hrs

    def calculate_emp_wage(self):

        total_emp_wage = 0
        total_emp_hrs = 0
        total_working_days = 0
        while total_working_days < self.maximum_working_days and total_emp_hrs < self.maximum_working_hrs:
            emp_hrs_per_day = self.get_emp_hrs()
            total_emp_wage += emp_hrs_per_day * self.wage_per_hour
            total_emp_hrs += emp_hrs_per_day
            total_working_days += 1
            print("working day: ", total_working_days, ":", total_emp_wage)

        return total_emp_wage

    def calculate_emp_wage_multiple_company(self, maximum_working_days, maximum_working_hrs, emp_per_hr_rate):

        total_emp_wage = 0
        total_emp_hrs = 0
        total_working_days = 0
        while total_working_days < maximum_working_days and total_emp_hrs < maximum_working_hrs:
            emp_hrs_per_day = self.get_emp_hrs()
            emp_daily_wage = emp_hrs_per_day * emp_per_hr_rate
            total_emp_wage += emp_daily_wage
            total_emp_hrs += emp_hrs_per_day
            total_working_days += 1
            print("working day: ", total_working_days, ":", total_emp_wage)

        return total_emp_wage


if __name__ == '__main__':
    '''
    created objects of EmployeeWage class and print the total monthly wage of employee
    '''
    emp_wage = EmployeeWage()
    print("total monthly wage of employee is: ", emp_wage.calculate_emp_wage())

    google = EmployeeWage()
    print("******************************* google employee **************************************")
    print("total monthly wage of employee working in google: ", google.calculate_emp_wage_multiple_company(20, 100, 20))
    ibm = EmployeeWage()
    print("******************************* ibm employee **************************************")
    print("total monthly wage of employee working in ibm: ", ibm.calculate_emp_wage_multiple_company(20, 50, 20))

