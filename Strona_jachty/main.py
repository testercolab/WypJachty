from flask import Flask, render_template, request, jsonify, request, url_for, flash, redirect
import json

from PrepareData import List, BoatData, BoatReservation, CN

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zaq1@WSX'

@app.route("/")
@app.route("/StronaGlowna")
def StronaGlowna():
	return render_template("StronaGlowna.html", title="Strona Główna")

@app.route("/Oferta")
def Oferta():
	return render_template("Oferta.html", title="Oferta", data=json.loads(List()))

@app.route("/OFirmie")
def OFirmie():
	return render_template("OFirmie.html", title="O firmie")

@app.route("/<int:Id>", methods=('GET', 'POST'))
def Szczegoly(Id):
	Alertclass = ""
	if request.method == 'POST':
		IsOk = False
		Od = request.form['od']
		Do = request.form['do']
		Imie = request.form['imie']
		Nazwisko = request.form['nazwisko']
		Nr = request.form['nr']
		if Od and Do and Imie and Nazwisko and Nr and len(Nr) == 9:
			IsOk = True
		if IsOk:
			Query = f"INSERT INTO rezerwacje (IdJacht, Od, Do, Imię, Nazwisko, NrTel) VALUES " \
					f"({Id}, '{Od}', '{Do}', '{Imie}', '{Nazwisko}', '{Nr}')"
			Result = CN.InsertData(Query)
			print(Result)
			print(Query)
			flash('Dokonano rezerwacji')
			Alertclass = "AlertGood"
		else:
			flash('Rezerwacja nie powiodła się')
			Alertclass = "AlertBad"

	return render_template("Szczegoly.html", title="Szczegóły", Alertclass=Alertclass,
						   Boatdata=json.loads(BoatData(Id)), Boatreservation=json.loads(BoatReservation(Id)))

if __name__ == "__main__":
	app.run(debug=True)