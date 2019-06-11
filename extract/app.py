from flask import Flask,jsonify


app = Flask(__name__)

tasks = [
{
'id':1,
'title':u'Buygroceries',
'description':u'Milk,Cheese,Pizza,Fruit,Tylenol',
'done': False
},
{
'id':2,
'title':u'LearnPython',
'description':u'Needto findagoodPythontutorial ontheweb',
'done': False
}
]
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods =['GET'])
def get_task(task_id):

	task= list(filter(lambda t: t['id']==task_id,tasks))
	if len(task)== 0:
		return "abort(404)"
	else:
		return jsonify( {'task':task[0]})
#for post
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
	if not request.json or not'title'in request.json:
		return "abort(400)"
		task={
		'id':tasks[-1]['id']+1,
		'title':request.json['title'],
		'description':request.json.get('description',""),
		'done': False
		}
	tasks.append(task)
	return jsonify( {'task':task }),201

if __name__ == '__main__':
	app.run(debug=True)