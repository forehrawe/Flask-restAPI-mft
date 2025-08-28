from flask import Flask, request, jsonify
from models import Student, Teacher, Grade
#curl -X POST http://localhost:5000/student -H "content-type:application/json" -d "{\"name\":\"hadi\", \"family\":\"ghes\",\"age\":\"20\" }"


app = Flask(__name__)


#---------------------------------STUDENT------------------------------------------------------------------

@app.route('/student', methods=['GET','POST'])
def student():
    if request.method == 'POST':
        data = request.get_json()
        Student.create(name=data['name'], family=data['family'], age=data['age'])
        return jsonify({'status':'200'}), 200
    
    students = Student.select()
    return jsonify([{'id':student.id, 'name':student.name, 'family':student.family, 'age':student.age } for student in students])

@app.route('/delst')
def deleteSt(id:int):
    student = Student.get_by_id(id)
    student.delete_instance()
    return jsonify({'status':'200'}), 200

@app.route('/updatest')
def updatest():
    id = request.args.get('id', type=int)
    newname = request.args.get('newname')
    newfam = request.args.get('newfam')
    newage = request.args.get('newage', type=int)
    st = Student.get_by_id(id)
    if newname:
        st.name = newname
        st.save()
    if newfam:
        st.family = newfam
        st.save()
    if newage:
        st.age = newage
        st.save()
    return jsonify({'status':'200'}), 200

#---------------------------------------TEACHER------------------------------------------------------------------




if __name__=='__main__':
    app.run(debug=True)