import unittest, sys, os

sys.path.append('../simple-webframe')
from demo import app, db

class UsersTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    ###############
    #### tests ####
    ###############

    def register(self, username, email, password, confirm_password):
        return self.app.post('/register',
                            data=dict(username=username,
                                      email=email,
                                      password=password, 
                                      confirm_password=confirm_password),
                            follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('test', 'test@example.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.assertEqual(response.status_code, 200)
         
         
    def test_invalid_username_registration(self):
        response = self.register('t', 'test@example.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.assertIn(b'Field must be between 2 and 20 characters long.', response.data)
      
    def test_invalid_email_registration(self):
        response = self.register('test2', 'test@example', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.assertIn(b'Invalid email address.', response.data)

#     def test_invalid_password_registration(self):
#         response = self.register('test3', 'test@example.com', 'FlaskIsAwesome', 'FlaskIsNOTAwesome')
#         self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()