import unittest
import db_functions
import hide
import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bankdatabase',
    password = hide.password
)
cursor = connection.cursor()



class TestFunctions(unittest.TestCase):
    def test_balance(self):
        self.assertEqual(db_functions.balance(57812, 5912), None)

    def test_getAccount(self):
        self.assertEqual(db_functions.getAccount(), [12345, 1234, 3750, 'Timmy', '1890 Creek Lane', '12/12/2012', 'yes'])

    def test_deposit(self):
        self.assertEqual(db_functions.deposit(57812, 5912), None)

    def test_withdraw(self):
        self.assertEqual(db_functions.withdraw(57812, 5912), None)
    
    def test_create_account(self):
        self.assertEqual(db_functions.create_account(), None)
    
    def test_close_account(self):
        self.assertEqual(db_functions.close_account(), None)
    
    def test_mod_account(self):
        self.assertEqual(db_functions.mod_account(), None)

    def test_check_admin(self):
        self.assertTrue(db_functions.check_admin(12345,1234))


if __name__ == '__main__':
    unittest.main()
