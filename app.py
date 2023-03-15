from flask import Flask,render_template,jsonify

app = Flask(__name__)


data = [{
    'role':'Data Analyst',
    'location':'Sambhaji Nagar',
    'salary': 150000

},{
    'role':'Data Miner',
    'location':'Sambhaji Nagar',
    'salary': 150000

},{
    'role':'Sales Person',
    'location':'Sambhaji Nagar',
    'salary': 150000

}

]


@app.route("/")
def main():
    return render_template('home.html',data=data)

@app.route('/api/jobs')
def get_jobs():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)