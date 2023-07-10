
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    schema="dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_one(cls, dojo_id):
        results = connectToMySQL(cls.schema).query_db("SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;", {'dojo_id': dojo_id})
        dojo = cls(results[0]) # create the main class from the first row
        # all rows contain info from the join
        for result in results:
            ninja_data = {
                "id": result["ninjas.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "age": result["age"],
                "dojo_id": result["dojo_id"],
                "created_at": result["ninjas.created_at"],
                "updated_at": result["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all(cls):
        results = connectToMySQL(cls.schema).query_db("SELECT * FROM dojos;")
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.schema).query_db(query, data)
