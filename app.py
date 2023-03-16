from flask import Flask,render_template,jsonify
from database import get_jobsdata


app = Flask(__name__)



@app.route("/")
def main():
    jobs= get_jobsdata()
    return render_template('home.html',data=jobs)

@app.route('/api/jobs')
def get_jobs():
    jobs_api = get_jobsdata()
    return jsonify(jobs_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)