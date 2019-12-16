from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_repler():
  return 'Hello, Repler!'

@app.route('/test')
def test_flask():
  return 'This is just a test'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)