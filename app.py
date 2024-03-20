from flask import Flask,render_template,redirect,url_for,request,session
from flask_mysqldb import MySQL
import pickle
import numpy as np
from forms import TestForm
from sklearn.cluster import KMeans
import random
app=Flask(__name__)

app.secret_key='karthick_studen_career_guidane'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='data'

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    if session['loggedin']:
        return render_template('index.html')
    else :
        return f"Please login in"

@app.route('/logout') 
def logout(): 
    session['loggedin']=False
    session.pop('id', None) 
    session.pop('username', None) 
    return redirect('/login') 

@app.route("/career_pred")
def career_prediction():
    return render_template('careertest.html')

@app.route('/12th')
def after_12th():
   return render_template('after12th.html')

@app.route('/login',methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        if cursor.execute(' SELECT * FROM user_accounts WHERE username=%s or password=%s ',(username,password)):
            if cursor.execute(' SELECT * FROM user_accounts WHERE username=%s and password=%s ',(username,password)):
                account=cursor.fetchone()
                session['loggedin'] = True
                session['id'] = account[0]
                session['name'] = account[1]
                session['username'] = account[3]
                return redirect('/index')
            elif cursor.execute(' SELECT * FROM user_accounts WHERE username=%s ',(username,)):
                return render_template('login.html',msg="Wrong password",username=username)
            else :
                return f"Invalid"
        else :
            return f"Invalid"
    else :
        return render_template('login.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        if cursor.execute(' SELECT * FROM user_accounts WHERE email=%s or username=%s ',(email,username)):
            if cursor.execute(' SELECT * FROM user_accounts WHERE email=%s and username=%s ',(email,username)):
                return render_template('register.html',msg="Email and Username already taken",name=name)
            elif cursor.execute(' SELECT * FROM user_accounts WHERE email=%s ',(email,)):
                return render_template('register.html',msg="Email already registered,try another email",name=name,username=username)
            elif cursor.execute(' SELECT * FROM user_accounts WHERE username=%s ',(username,)):
                return render_template('register.html',msg="Username already exists,try another username",name=name,email=email)
        else :
            cursor.execute(' INSERT INTO user_accounts (Name,Username,Email,Password) VALUES(%s,%s,%s,%s) ',(name,username,email,password))
        mysql.connection.commit()
        cursor.close()
        return redirect('/')
    else :
        return render_template('login.html')

@app.route('/courses')
def courses_view():
    return render_template('courses.html')

@app.route('/blank')
def blnk():
    return render_template('blank_page.html')


@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      i = 0
      print(result)
      res = result.to_dict(flat=True)
      print("res:",res)
      arr1 = res.values()
      arr = ([value for value in arr1])

      data = np.array(arr)

      data = data.reshape(1,-1)
      print(data)
      loaded_model = pickle.load(open("careerlast.pkl", 'rb'))
      

      print(loaded_model)
      predictions = loaded_model.predict(data)
      #return render_template('testafter.html',a=predictions)
      #print("================================================================")
      #print(predictions)
      pred = loaded_model.predict_proba(data)
      #print(pred)
      #acc=accuracy_score(pred,)
      pred = pred > 0.05
      i = 0
      j = 0
      index = 0
      res = {}
      final_res = {}
      while j < 17:
          if pred[i, j]:
              res[index] = j
              index += 1
          j += 1

      index = 0
      for key, values in res.items():
          if values != predictions[0]:
              final_res[index] = values
              print('final_res[index]:',final_res[index])
              index += 1
      #print(final_res)
      jobs_dict = {0:'AI ML Specialist',
                   1:'API Integration Specialist',
                   2:'Application Support Engineer',
                   3:'Business Analyst',
                   4:'Customer Service Executive',
                   5:'Cyber Security Specialist',
                   6:'Data Scientist',
                   7:'Database Administrator',
                   8:'Graphics Designer',
                   9:'Hardware Engineer',
                   10:'Helpdesk Engineer',
                   11:'Information Security Specialist',
                   12:'Networking Engineer',
                   13:'Project Manager',
                   14:'Software Developer',
                   15:'Software Tester',
                   16:'Technical Writer'}               
      job = {}
      index = 1
      data1=predictions[0]
      print(data1)
      return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
   

# psychometric test cmd
def yon():
    a = random.choice([0, 1])
    return a

X = np.array([[yon() for _ in range(10)] for _ in range(300)])
# print(X)
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# print(centroids)
# print(labels)   

def decision(num):
    base = "you belong to"
    if num == 1:
        return base + " leaders"
    elif num == 2:
        return base + " Emotionals"
    elif num == 3:
        return base + " Hard Workers"
    elif num == 4:
        return base + " Smart Workers"
    else:
        return base + " visionaries"


@app.route('/psycho-metric-test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        Q1 = int(request.form['Q1'])
        Q2 = int(request.form['Q2'])
        Q3 = int(request.form['Q3'])
        Q4 = int(request.form['Q4'])
        Q5 = int(request.form['Q5'])
        Q6 = int(request.form['Q6'])
        Q7 = int(request.form['Q7'])
        Q8 = int(request.form['Q8'])
        Q9 = int(request.form['Q9'])
        Q10 = int(request.form['Q10'])

        tlist = (Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10)
        error = []
        for cet in centroids:
            error.append(sum(np.square(np.subtract(cet, tlist)))) 
        result = error.index(min(error))
        # print(result)
        return render_template('psychometric_result.html', result=decision(result))
    form=TestForm()
    return render_template('psychometric_test.html',form=form)
if __name__ == "__main__":
    app.run(debug=False)