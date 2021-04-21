from keras.models import load_model
from flask import Flask , render_template , request

app = Flask('diabetes_model_app')
model = load_model('diabetes_model.h5')

@app.route("/home")
def home():
    return render_template("form.html")

@app.route("/output" , methods=[  "GET"  ])
def dia():
        x1 = request.args.get("z1")
        x2 = request.args.get("z2")
        x3 = request.args.get("z3")
        x4 = request.args.get("z4")
        x5 = request.args.get("z5")
        x6 = request.args.get("z6")
        x7 = request.args.get("z7")
        x8 = request.args.get("z8")
        output=model.predict([[int(x1),int(x2),int(x3),int(x4),int(x5),float(x6),float(x7),int(x8)]])
        o=str(round(output[0][0]))
        if o=='0':
          return ("<h1><center><body bgcolor='green'>Not Diabetic</h1>")
        else:
          return("<h1><center><body bgcolor=red<font color=white><b>Most likely to be diabetic</b></h1>")

app.run('0.0.0.0')
