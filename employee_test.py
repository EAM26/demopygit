import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('john', 'smith', 40000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(45000, self.my_employee.annual_salary)

    def test_give_custom_raise_(self):
        self.my_employee.give_raise(3000)
        self.assertEqual(43000, self.my_employee.annual_salary)

if __name__ == '__main__':
    unittest.main()




