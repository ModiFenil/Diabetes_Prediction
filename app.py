from flask import Flask,render_template,request
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

model = pickle.load(open("model/Diabetes_model.pkl","rb"))

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/new',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        pregnencies = int(request.form.get("pregnancies"))
        glucose = float(request.form.get("glucose"))
        bloodpressure = float(request.form.get("bloodpressure"))
        skinthickness = float(request.form.get("skinthickness"))
        insulin = float(request.form.get("insulin"))
        bmi = float(request.form.get("bmi"))
        diabetespedigreefunction = float(request.form.get("diabetespedigreefunction"))
        age = float(request.form.get("age"))
        
        predict = model.predict([[pregnencies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]])
        
        if predict[0] == 1:
            result = "Diabetic"
        else:
            if predict[0] == 0:
                result = "Non-Diabetic"
        return render_template("result.html",result=result)
    else:
        return render_template("index.html")
    
if __name__ == "__main__":
    app.run(port=5000)