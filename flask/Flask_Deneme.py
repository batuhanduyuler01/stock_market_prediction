import modeli_calistir
import veri_cek
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

#direkt route'a yönlendir
@app.route("/")
def index():
	garanti_test, X_test = veri_cek.test_verisini_cek()
	tahmin, trend = modeli_calistir.trendbul(X_test, garanti_test)
	yatirim = []
	yatirim.append(trend)

    

	return render_template("index.html", predict = tahmin, data = yatirim)


if __name__ == "__main__":
    app.run(debug=True)




#@app.route("/predict", methods=['POST'])
#def predict():
    
#    garanti_test , X_test = veri_cek.test_verisini_cek()

#    tahmin, trend = modeli_calistir.trendbul(X_test, garanti_test )
    
#    return render_template('index.html', predict = tahmin)

#@app.route('/results', methods = ['POST'])
#def results():
	#garanti_test , X_test = veri_cek.test_verisini_cek()
	#tahmin, trend = modeli_calistir.trendbul(X_test, garanti_test )
	#output = trend
	#return jsonify(output)

