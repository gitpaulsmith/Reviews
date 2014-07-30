from flask import Flask, render_template,request,redirect
import numpy as np
import pandas as pd
import io
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


#from random import randint

def predict(X):
	return clf.predict(X)

def score(prediction, actual):
	return clf.score(prediction,actual)

def saveScores(userScore,ourScore):
	filename="results.csv"
	f=open(filename,'a')
	np.savetxt(f,np.column_stack((userScore,ourScore)),fmt=('%.3f,%0.3f'))
	f.close()

def readScores():
	filename="results.csv"
	f=open(filename,'r')
	userscores,ourscores=np.loadtxt(f,delimiter=',',unpack='True')
	return np.mean(userscores),np.mean(ourscores)
 	
app = Flask(__name__)

def decodeArray(text):
    try:
        return text.decode("utf-8","replace")
    except:
        return 0

def loadReviews(n):
	fn='reviews.csv'
	f = open(fn,'r')
	df = pd.read_csv(f,engine='python')
	f.close()
	indexes=np.round(np.random.rand(n)*5000)
	indexes=indexes.astype(int)
	reviews=[]
	scores=[]
	productIds=[]
	
	for index in indexes:
	    reviews=np.append(reviews,decodeArray(df.iloc[index]['text']))
	    scores=np.append(scores,df.iloc[index]['score'])
    	productIds=np.append(productIds,df.iloc[index]['productId'])
	return reviews,scores,productIds

@app.route('/results', methods = ['POST'])
def results():
	userPred=np.zeros(10)
	ourPred=predict(reviews)
	#ourPred=[1,3,4,5,2,1,3,5,3,4]
	for i in range(10):
		userPred[i]=request.form['input-'+str(i+1)]

	userScore=accuracy_score(userPred,scores)
	ourScore=accuracy_score(ourPred,scores)
	
	saveScores(userScore,ourScore)
	userCumulative,ourCumulative=readScores()

	chart = {"renderTo": 'chart_ID', "type": 'bar', "height": 350, "width": 350,}
	series = [{"name": 'Prediction', "data": [userScore,ourScore]},{"name": 'Cumulative Prediction', "data": [userCumulative,ourCumulative]}]

	message="Your score is "+str(accuracy_score(userPred,scores))+" and our score is "+str(accuracy_score(ourPred,scores))+"."
	return render_template('home.html',text=message,UserRatings=userPred, OurRatings=ourPred, reviews=reviews,scores=scores,showScores=True, 
		chartID='chart_ID', chart=chart, series=series)

@app.route('/')
def home(message=""):
	#reviews, scores, Ids=loadReviews(10)
	global reviews, scores, Ids
	reviews, scores, Ids=loadReviews(10)
	message="Guess the star rating for the following 10 reviews:"
	return render_template('home.html',text=message,reviews=reviews,scores=scores,showScores=False)

@app.route('/about')
def about():
  return render_template('about.html')
 
if __name__ == '__main__':
	global clf
	NB_file="model/multiclass_NB.joblib.pkl"
	clf = joblib.load(NB_file)
  	app.run(debug=True)