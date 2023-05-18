from app import app
from flask import render_template
@app.route('/') # www.example.com
@app.route('/index') # www.example.com/index
def index():
    kullanici = {"kullaniciadi":"UZAKTAN EĞİTİM 2222222"}
    selam = "Hellooooooooo"
    veriler = [
        {
            "adi":"İbrahim",
            "soyadi":"EDİZ"
        },
        {
            "adi":"Cihan",
            "soyadi":"HAKAN"
        },
    ]
    return render_template("index.html",kullanici=kullanici,veriler=veriler)