#Hadi Ghesmatpour
from flask import Flask, request, jsonify
from models import Student, Teacher, Grade, DoesNotExist

app = Flask(__name__)


#--------------------------------------------------Student--------------------------------------------

@app.route('/student', methods=['GET','POST'])
def student():
    if request.method == 'POST':
        data = request.get_json()
        Student.create(name=data['name'], family=data['family'], age=data['age'])
        return jsonify({'status':'200'}), 200
    
    students = Student.select()
    return jsonify([{'id':student.id, 'name':student.name, 'family':student.family, 'age':student.age} for student in students])

@app.route('/student', methods=['PUT'])
def update_student():
    data = request.get_json()
    id = data['id']
    newname = data.get('name')
    newfam = data.get('family')
    newage = data.get('age')
    row = Student.get_by_id(id)
    
    response = {}
    
    if newname:
        row.name = newname
        row.save()
        response['name'] = 'changed'
        
    if newfam:
        row.family = newfam
        row.save()
        response['family'] = 'changed'
        
    if newage:
        if newage.isnumeric():
            row.age = newage
            row.save()
            response['age'] = 'changed'
            
    return jsonify(response), 200
    
@app.route('/student', methods=['DELETE'])
def del_st():
    data = request.get_json()
    id = data['id']
    try:
        st = Student.get_by_id(id)
        st.delete_instance()
    except DoesNotExist:
        return jsonify({'status':'DoesNotExists'}), 400
    

#------------------------------------------------TEACHERS---------------------------------------------

@app.route('/teacher', methods=['GET','POST'])
def teachers():
    if request.method == 'POST':
        data = request.get_json()
        Student.create(name=data['name'], family=data['family'], subject=data['subject'])
        return jsonify({'status':'200'}), 200
    
    teacher = Teacher.select()
    return jsonify([{'id':teacher.id, 'name':teacher.name, 'family':teacher.family, 'subject':teacher.subject} for teacher in teachers])

@app.route('/teacher', methods=['PUT'])
def update_teacher():
    data = request.get_json()
    id = data['id']
    newname = data.get('name')
    newfam = data.get('family')
    newsub = data.get('subject')
    row = Teacher.get_by_id(id)
    
    response = {}
    
    if newname:
        row.name = newname
        row.save()
        response['name'] = 'changed'
        
    if newfam:
        row.family = newfam
        row.save()
        response['family'] = 'changed'
        
    if newsub:
        row.age = newsub
        row.save()
        response['Subject'] = 'changed'
            
    return jsonify(response), 200
    
@app.route('/teacher', methods=['DELETE'])
def del_tc():
    data = request.get_json()
    id = data['id']
    try:
        st = Teacher.get_by_id(id)
        st.delete_instance()
    except DoesNotExist:
        return jsonify({'status':'DoesNotExists'}), 400

#------------------------------------------------------Grade-----------------------------------------------------

@app.route('/grade', methods=['GET','POST'])
def grade():
    if request.method == 'POST':
        data = request.get_json()
        Grade.create(teacher=data['teacher'], student=data['student'], grade=data['grade'])
        return jsonify({'status':'200'}), 200
    
    grades = Grade.select()
    return jsonify([{'id':grade.id,'teacher':grade.teacher_id,'student':grade.student_id, 'grade':grade.grade} for grade in grades])

@app.route('/grade', methods=['PUT'])
def update_grade():
    data = request.get_json()
    id = data['id']
    newgrade = data['grade']
    
    try:
        row = Grade.get_by_id(id)
        row.grade = newgrade
        row.save()
        return jsonify({'status':'200'}),200
    except DoesNotExist:
        return jsonify({'status':'doesNotExists'}), 404
    
    
@app.route('/grade', methods=['DELETE'])
def del_grade():
    data = request.get_json()
    id = data['id']
    try:
        st = Grade.get_by_id(id)
        st.delete_instance()
        return jsonify({'status':'200'}),200
    except DoesNotExist:
        return jsonify({'status':'doesNotExists'}), 404


if __name__=='__main__':
    app.run(debug=True)