from flask import Flask,render_template,jsonify
from database import cnx

app = Flask(__name__)



def get_jobsdata():
    cursor = cnx.cursor()
    with cursor as cur:
        print('connection successful')
        cur.execute("SELECT * FROM jobs");
        # get column names
        columns = [col[0] for col in cur.description]
        results = cursor.fetchall()
        result_dict = []
        for row in results:
            result_dict.append(dict(zip(columns,row)))
        #printing the results dict
        return result_dict







@app.route("/")
def main():
    jobs= get_jobsdata()
    return render_template('home.html',data=jobs)

@app.route('/api/jobs')
def get_jobs():
    jobs_api = get_jobsdata()
    return jsonify(jobs_api)


if __name__ == '__main__':
    app.run(debug=True)