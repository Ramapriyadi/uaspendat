
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "HAYYYYY"

# @app.route('/login', methods=['POST','GET'])
# def index():
#   if request.method == 'POST':
#     return render_template('index.html')
  
#   else:
#     return render_template('index.html')

# if __name__ =="__main__":
#   app.run(debug=True)