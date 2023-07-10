
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    schema="user_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (name, email, password) VALUES (%(name)s, %(email)s, %(password1)s);"
        return connectToMySQL(cls.schema).query_db(query, data)
    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s AND users.password = %(password1)s"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if not all(results):
            return None
        return cls(results[0])