
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    schema="users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, user_id):
        results = connectToMySQL(cls.schema).query_db("SELECT * FROM users WHERE users.id = %(user_id)s;", {'user_id': user_id})
        return cls(results[0])

    @classmethod
    def get_all(cls):
        results = connectToMySQL(cls.schema).query_db("SELECT * FROM users;")
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.schema).query_db(query, data)

    @classmethod
    def edit_user(cls, data):
        query = """
        UPDATE users SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.schema).query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        return connectToMySQL(cls.schema).query_db("DELETE FROM users WHERE id = %(id)s", data)
