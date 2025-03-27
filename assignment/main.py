from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from flask import Flask,render_template,request
import tm
import time
import random
import base64
import mains
import yolo

app=Flask(__name__)



@app.route('/')
def inded():
    return render_template('index.html')




@app.route("/tema",methods=["POST","GET"])
def teach():
    if request.method=="GET":
        return render_template('tekil.html')  
    elif request.method=="POST":
        xq=request.form.get("x")
        print(xq)
        mains.sel(xq)

        return render_template('secim.html')   

@app.route('/<int:x>') 
def answer(x):
    cevap=''
    sonuc=''
    
    if x==1:
       sonuc= tm.start(f'./static/img/a.png')
    elif x==2:
        sonuc=tm.start(f'./static/img/b.png')
    elif x==3:
        sonuc=tm.start(f'./static/img/c.png')
    else:
        sonuc='7777777777777777777777777777777777777777777'
        print('Sonuc bulanamadı')
    
    if sonuc=='insan':
        cevap='Arattığınız varlık bir insan'
    elif sonuc=='spor':
        cevap='Arattığınız varlık bir spor malzemesi'
    elif sonuc=='otomotiv':
        cevap='Arattığınız varlık bir otomobil'
    elif sonuc=='hayvan':
        cevap='Arattığınız varlık bir hayvan'
    elif sonuc=='bitki':
        cevap='Arattığınız varlık bir bitki'
    elif sonuc=='ayakkabı':
        cevap='Arattığınız varlık bir ayakkabı'
    else:
        cevap='Anlamadım.'

    return render_template('result.html',cevap=cevap)




@app.route('/yolo',methods=['POST','GET'])
def yolov():
    if request.method=='GET':
        return render_template('searchc.html')
    elif request.method=='POST':
        cogul=request.form.get("thing")
        mains.sel(cogul)
        return render_template('secim.html')
    
@app.route('/<int:y>')
def resultyolo(y):
    sonuc=''
    if y==1:
        sonuc= yolo.yolo(f'./static/img/a.png')
    if y==2:
        sonuc= yolo.yolo(f'./static/img/b.png')
    if y==3:
        sonuc= yolo.sayim(yolo.yolo(f'./static/img/c.png'))
    return render_template('result.html',sonuc=sonuc)



app.run(debug=True)

