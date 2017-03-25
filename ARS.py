from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_file', methods=['POST'])
def create_file():
    print(request.json)
    with open('/home/viviana/PycharmProjects/ARS/file.csv', 'w+') as f:
        c = csv.DictWriter(f, ['cedula', 'monto'])
        c.writeheader()
        c.writerows(request.json)
    return redirect('/')

if __name__ == '__main__':
    app.run()
