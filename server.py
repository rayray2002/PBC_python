from flask import Flask, request, session, redirect
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def hello_world():
    username = session.get("username", "guest")
    return f'Hello, {username}'


@app.route("/p", methods=["POST"])
def p():
    return "post page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        print(session)
        return redirect("/")
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


if __name__ == "__main__":
    app.run(port=8000)
