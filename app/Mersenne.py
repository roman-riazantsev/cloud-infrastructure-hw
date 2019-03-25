from flask import Flask, render_template
import math

app = Flask(__name__)


k = 0
m_list = []

@app.route('/start')
def start():
  def primes(n):
      """ Return a list of the prime numbers <= n. """

      sieve = [True] * (n // 2)
      for i in range(3, int(math.sqrt(n))+1, 2):
          if sieve[i//2]:
              sieve[i*i//2::i] = [False] * ((n - i*i - 1) // (2*i) +1)
      return [2] + [2*i+1 for i in range(1, n // 2) if sieve[i]]

  def calc_merser(n):
      global m_list
      P = set(primes(n))

      # A list of integers 2^i-1 <= n
      A = []
      for i in range(2, int(math.log(n+1, 2))+1):
          A.append(2**i - 1)

      # The set of Mersenne primes as the intersection of P and A
      M = P.intersection(A)

      # Output as a sorted list of M
      m_list = sorted(list(M))

  for i in range(90):
      global k
      k+=1
      calc_merser(100000000)

  return "calculated merser 90 times for number 100000000"

@app.route('/stop')
def stop():
  output = "Mersenne primes: {}, calculated: {} times".format(m_list, k)
  return output

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
