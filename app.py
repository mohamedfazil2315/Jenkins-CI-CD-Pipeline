from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home(): 
	return "Its Fazil's Flask App "

@app.route("/about") 
def about(): 
	return "Welcome the Sagaa Web App 5"
    
@app.route("/contact") 
def contact(): 
	return "<h1>FLASK DEMO FOR CI CD Pipeline</H1>"

@app.route("/testform")
def testform():
    if request.method=='GET':
        return render_template('myform.html')
	
@app.route("/addtest") 
def addtest(): 
	a = request.args.get("a")
	b = request.args.get("b")

	result = int(a) + int(b)

	return "<h1>" + str(result) + "</h1>"


if __name__ == "__main__":
	app.run(
        host="0.0.0.0",   # VERY IMPORTANT
        port=5000,
        debug=False
    )
