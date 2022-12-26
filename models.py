from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Model_name(db.Model):
    __tablename__ = 'table_name'
 
    field1_name = db.Column(db.Field1Type, primary_key)
    field2_name = db.Column(db.Field2Type)
    field3_name = db.Column(db.Field3Type)
 
    def __init__(self, Field1_name,Field2_name,Field3_name):
        self.field1_name = field1_name
        self.field2_name = field2_name
        self.field3_name = field3_name
 
    def __repr__(self):
        return f"<statement>"