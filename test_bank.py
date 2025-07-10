import unittest
from bank_account import BankAccount 

"""
description: 


"""

class TestBank(unittest.TestCase):
    def setUp(self):
        self.p1 = BankAccount("p1", 1, 100)
        self.p2 = BankAccount("p2", 2, 200)
        self.p3 = BankAccount("p3", 3, 300)

    def test_balance(self):
        self.assertEqual(self.p1.get_balance(), 100)
        self.assertEqual(self.p2.get_balance(), 200)
        self.assertEqual(self.p3.get_balance(), 300)

    def test_withdraw(self):
        self.p1.withdraw(50)
        self.assertEqual(self.p1.get_balance(), 50)
        self.assertEqual(self.p1.balance(), 50)
        self.p2.withdraw(50)
        self.assertEqual(self.p2.get_balance(), 150)
        self.p3.withdraw(50)
        self.assertEqual(self.p3.get_balance(), 250)

    def test_deposit(self):
        self.p1.deposit(100)
        self.assertEqual(self.p1.get_balance(), 200)
        self.p2.deposit(100)
        self.assertEqual(self.p2.get_balance(), 300)
        self.p3.deposit(100)
        self.assertEqual(self.p3.get_balance(), 400)