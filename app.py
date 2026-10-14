from flask import Flask,render_template,request, jsonify

app=Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html",name="Meghana",role="Engineer",score=65,
                           skills=[])#["python","SQL","React","Flask"])

@app.route("/review",methods=["POST"])
def review():
    username=request.form.get("username","").strip()

    if not username:
        return "Please enter your name.",400
    
    return render_template("review.html",username=username,length=len(username))

@app.route("/search",methods=["GET"])
def search():
    skill=request.args.get("skill","").strip()

    if not skill:
        return "Please provide a skill to search for.",400
        
    if skill.lower()=="python":
        description="Python is used for scripting, backend development, and data analysis."

    elif skill.lower()=="react":
        description="React is used to build user interfaces."

    elif skill.lower()=="sql":
        description="SQL is used to maintain and work on Databases."
    
    else :
        description="Your skill is used in software technologies, building projects."

    return render_template("search.html",skill=skill,description=description)

@app.route("/api/status",methods=["GET"])
def api_status():
    return jsonify({
        "project":"AI Resume Reviewer",
        "status":"running"
    })

if __name__ =="__main__":
    app.run()