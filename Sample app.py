from flask import Flask, request , render_template

app = Fask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
      return 'Logged in successfully!'
    else:
      return 'Invalid username or password'
    return render_template('login.html')

if __name__ == '__main__':
  app.run(debug=true)  