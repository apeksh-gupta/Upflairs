from flask import Flask ,render_template , request , jsonify 
import joblib
import pandas as pd

df = pd.read_csv("data_to_be_filtered.csv")

model = joblib.load("kmeans_model.lb")
standardscalar = joblib.load("StandardScaler.lb")

def find_label( x ):
    group = df[df["group_15"] == x]
    return list(  group["label"].value_counts().keys() )

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input")
def input():
    return render_template("input.html")
    

@app.route("/prediction" , methods = {"GET" , "POST"})
def prediction():
    if request.method == "POST":
        nitrogen = float(request.form['nitrogen'])
        phosphorous = float(request.form['phosphorous'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity= float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        data = [ nitrogen , phosphorous , potassium ,temperature ,  humidity , ph , rainfall]
        transformed_data = standardscalar.transform([data])
        pred = model.predict(transformed_data)
        labels = find_label(pred[0])
        return render_template("prediction.html" , crops = labels , group_no = pred )



if __name__ == "__main__":
    app.run(debug=True)