import os
...
port = int(os.environ.get('PORT', 5000))
...
app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
  if request.method == 'POST':
    return render_template('results.html')
  
  else:
    return render_template('index.html')

if __name__ =="__main__":
  app.run(debug=True)