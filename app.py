from flask import Flask,render_template, request, jsonify
from src.carrer_recommendations import carrer_recommendation
from src.carrer_pathways import carrer_pathways

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
   return render_template('home.html')

@app.route('/recommend',methods=['GET','POST'])
def career_recommendations():
    if request.method=='POST':
        Name = request.form['name']
        Skills = request.form['skills']
        Education = request.form['education']
        user_profile={
            "name":Name,
            "skills":Skills,
            "education":Education
        }
    carrer=carrer_recommendation(user_profile)
    
    recommendations=[]
    for rec in carrer.get("Recommendations", []):
    
        recommendations.append(
            {
                "Carrer":rec.get("Carrer"),
                "match_percent":rec.get("match_percent"),
                "Description":rec.get("Description"),
            
            }
        )
    return render_template('carrer_recommendations.html', user_name=carrer.get("user_name", user_profile["name"]),
            recs=recommendations
        )
@app.route("/pathways/<career_name>", methods=["GET"])
def pathways(career_name):
   
    pathways = carrer_pathways(
        courses=career_name.replace("-", " ").title(),
        skills="Python, Machine Learning, Statistics",
        education="Bachelor's"
    )
    return render_template("pathways.html",carrer_name=pathways.get("Carrer", career_name.replace("-", " ").title()),
        roadmap=pathways.get("roadmap", []),
        courses=pathways.get("Courses", []),
        projects=pathways.get("Projects", [])
    )



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


