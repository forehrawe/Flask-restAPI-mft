from peewee import SqliteDatabase, Model, CharField,IntegerField, ForeignKeyField

db = SqliteDatabase('mydb.db') 

class Basemodel(Model):
    class Meta:
        database = db
        
        
class Teacher(Basemodel):
    name = CharField(max_length=10)
    family = CharField(max_length=15)
    sucject = CharField(max_length=40)

class Student(Basemodel):
    name = CharField(max_length=10)
    family = CharField(max_length=15)
    age = IntegerField()
    
class Grade(Basemodel):
    teacher = ForeignKeyField(Teacher, on_delete='CASCADE')
    student = ForeignKeyField(Student, on_delete='CASCADE')
    grade = IntegerField()
    
db.connect()
db.create_tables([Teacher, Student, Grade])