from flask import Flask
#import numpy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  #result = ""
  #result_t, result_x = rk4(f, 0, np.array([np.pi/4, 0]), 100, 0.1)
  #return str(result_x)
  return "ququshka"
  
if __name__ == '__main__':
  app.run()
