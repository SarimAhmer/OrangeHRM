import unittest
from selenium import webdriver
from test_AddUser import AddUser

class TestUserCreation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.add_user_page = AddUser(self.driver)
        self.add_user_page.useradd()

    def test_user_creation(self):
        created_user = self.add_user_page.VerifyUser()
        self.assertIsNotNone(created_user, "User creation failed.")
        self.assertTrue(created_user.startswith(created_user), "User name doesn't match")

    def tearDown(self):
        # Perform any necessary cleanup (e.g., deleting the created user)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
