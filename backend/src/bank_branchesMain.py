import pandas as pd
from flask import Flask , jsonify , request
from flask_sqlalchemy import SQLAlchemy
import json
import sys
import os.path
from flask_cors import CORS

current_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(current_path, "./../bank_branches.csv")
bank_branches = pd.read_csv(data_path)
app = Flask(__name__)


CORS(app)
app.config['SQLALCHEMY_Track_MODIFICATIONS'] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route('/bank/ifsc/')
def get_bankDetails_ifsc():
	ifsc = request.args.get('ifsc', None)
	print(ifsc)
	return bank_branches[bank_branches['ifsc']==ifsc].to_json(orient='records')

@app.route('/bank/branch/')
def get_bankDetails_branch():
	city = request.args.get('city',None)
	branch = request.args.get('branch',None)
	if(city != None):
		city = city.upper()
	if(branch != None):
		branch = branch.upper()
	return bank_branches[(bank_branches['city']==city) & (bank_branches['branch']==branch)].to_json(orient='records')

app.run(port=5000)

