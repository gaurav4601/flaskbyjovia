from flask import Flask,render_template,jsonify,request
from database import get_jobsdata
from application import apply_job


app = Flask(__name__)



@app.route("/")
def main():
    jobs= get_jobsdata()
    return render_template('home.html',data=jobs)

@app.route('/api/jobs')
def get_jobs():
    jobs_api = get_jobsdata()
    return jsonify(jobs_api)


@app.route('/jobs/<int:id>')
def get_sjob(id):
    job = get_jobsdata(id)
    return render_template('1.html',title=job[0]['title'],job=job)

@app.route('/application',methods=["POST","GET"])
def application():
    if request.method == "POST":
        name = request.form.get('fname')
        age = request.form.get('fage')
        mbno = request.form.get('fmbno.')
        apply_job(name=name,age=age,mobile=mbno)
        return render_template('home.html')
    else:
        print(request.form)
        print(request.method)
        return 'Error in Page 404' 
    
@app.route('/contact')
def contact():
    return render_template('personal.html')  
     



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)