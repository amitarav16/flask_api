from flask import Flask, render_template, request
import requests
import json
import re
#imports
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag,StanfordNERTagger
from geograpy import extraction
from date_extractor import extract_dates
import datefinder


app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		inp =  request.form.to_dict()

		return render_template("result.html",result = inp)

if __name__ == '__main__':
   app.run(debug = True)













