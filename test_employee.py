import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.empl_1 = Employee("John", "Doe", 50000)
        self.empl_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.empl_1.email, "John.Doe@email.com")
        self.assertEqual(self.empl_2.email, "Sue.Smith@email.com")

        self.empl_1.first = "Joe"
        self.empl_2.first = "Lucy"

        self.assertEqual(self.empl_1.email, "Joe.Doe@email.com")
        self.assertEqual(self.empl_2.email, "Lucy.Smith@email.com")

    def test_fullname(self):
        self.assertEqual(self.empl_1.fullname, "John Doe")
        self.assertEqual(self.empl_2.fullname, "Sue Smith")

        self.empl_1.first = "Joe"
        self.empl_2.first = "Lucy"

        self.assertEqual(self.empl_1.fullname, "Joe Doe")
        self.assertEqual(self.empl_2.fullname, "Lucy Smith")

    def test_apply_raise(self):
        self.empl_1.apply_raise()
        self.empl_2.apply_raise()

        self.assertEqual(self.empl_1.pay, 52500)
        self.assertEqual(self.empl_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            schedule = self.empl_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://example.com/Doe/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.empl_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://example.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")
