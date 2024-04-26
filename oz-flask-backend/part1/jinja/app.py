from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

    # title = 'flask Jinja Template'
    # (1)rendering 할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', users = users)

if __name__ == "__main__":
    app.run(debug = True)


#호출값
# User_names
# Alex (traveler)
# Sam (photographer)
# Chris (gourmet)