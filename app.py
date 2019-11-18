import numpy as np
from flask import Flask, request

def f(t, x, g=9.8, l=1):
  theta, ang_vel  = x[0], x[1]
  return np.array([ang_vel, -g*np.sin(theta)/l])

def next_x(F, t, x, dt):
  k1 = F(t, x)
  k2 = F(t + dt/2, x + dt*k1/2)
  k3 = F(t + dt/2, x + dt*k2/2)
  k4 = F(t + dt, x + dt*k3)
  return x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
  
def rk4(F, t0, x0, t, dt=0.1):
  t_array = np.arange(t0, t+dt, dt)
  t_array[-1] = t

  x_array = np.zeros((t_array.size, x0.size), dtype = float)
  x_array[0] = x0

  for i in range(1, t_array.size - 1):
    x_array[i] = next_x(F, t_array[i-1], x_array[i-1], dt)

  x_array[-1] = next_x(F, t_array[-2], x_array[-2], t_array[-1] - t_array[-2])
  return t_array, x_array

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(dt="0.1"):
    result_t, result_x = rk4(f, 0, np.array([np.pi/4, 0]), 100, float(dt))
    return str(result_x[0])
  
if __name__ == '__main__':
    app.run()
