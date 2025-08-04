from flask import Flask, render_template, request

app = Flask(__name__)

facilities = [
    {"name": "青山図書館", "type": "図書館", "location": "青山キャンパスA棟", "opening_hours": "8:00-22:00"},
    {"name": "学生食堂", "type": "食堂", "location": "青山キャンパスB棟", "opening_hours": "11:00-20:00"},
    {"name": "体育館", "type": "スポーツ", "location": "青山キャンパスC棟", "opening_hours": "9:00-21:00"}
]

@app.route('/')
def index():
    keyword = request.args.get('q', '')
    filtered = [f for f in facilities if keyword in f["name"] or keyword in f["type"]]
    return render_template('index.html', facilities=filtered)

if __name__ == '__main__':
    app.run(debug=True)
