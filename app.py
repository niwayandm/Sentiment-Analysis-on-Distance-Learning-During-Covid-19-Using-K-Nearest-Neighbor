from flask import Flask, render_template
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

app = Flask(__name__)

model = pickle.load(open('model/knn_model.sav','rb'))
vectorizer = pickle.load(open("model/vectorizer.pickle", 'rb'))

filename = 'data/dataclean.csv'
data = pd.read_csv(filename, header=0)
myData = data.values


@app.route("/")
def layout():
    return render_template("home.html")

@app.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('home.html')

@app.route('/dataset', methods=['GET', 'POST'])
def dataset ():
    return render_template('dataset.html',myData=myData)

@app.route('/preprocessing', methods=['GET', 'POST'])
def dataclean ():
    
    return render_template('data_clean.html',myData=myData)

@app.route('/casefolding', methods=['GET', 'POST'])
def casefolding ():
    return render_template('case_folding.html',myData=myData)

@app.route('/normalizing', methods=['GET','POST'])
def normalizing ():
    return render_template('normalizing.html',myData=myData)

@app.route('/tokenizing', methods=['GET','POST'])
def tokenizing ():
    return render_template('tokenizing.html',myData=myData)

@app.route('/filtering', methods=['GET','POST'])
def filtering ():
    return render_template('filtering.html',myData=myData)

@app.route('/stemming', methods=['GET','POST'])
def stemming ():
    return render_template('stemming.html',myData=myData)

@app.route('/accuracy', methods=['GET','POST'])
def accuracy():
    filename = 'data/hasilklasifikasi.xlsx'
    data = pd.read_excel(filename, header=0)
    hasil = data.values
    return render_template('accuracy.html', hasil=hasil)

@app.route('/about', methods=['GET','POST'])
def about ():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()