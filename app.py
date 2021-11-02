from flask import Flask,render_template,url_for,request,jsonify
import spacy

# import en_core_web_sm
nlp = spacy.load('en_core_web_md')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		choice = request.form['taskoption']
		rawtext = request.form['rawtext']
		doc = nlp(rawtext)
		
		print("choice = ", choice)
		print("rawtext = ", rawtext)
		
		results = [(ent.label_, ent.text) for ent in doc.ents if ent.label_ == choice]
		
		num_of_results = len(results)
		# print(results)
		# print("num_of_results = ", num_of_results)
		
	return render_template("index.html",results=results,num_of_results = num_of_results)

if __name__ == '__main__':
	app.run(debug=True)
