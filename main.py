from flask import Flask, render_template
import yaml
from flask_mail import Mail, Message

app = Flask(__name__)
app.debug = True

with open('configuration.yaml') as file:
    mailParam = yaml.load(file, Loader=yaml.FullLoader)

mail= Mail(app)
app.config['MAIL_SERVER']=mailParam['mail']['host']
app.config['MAIL_PORT']=mailParam['mail']['port']
app.config['MAIL_USERNAME']=mailParam['mail']['username']
app.config['MAIL_PASSWORD']=mailParam['mail']['password']
app.config['MAIL_USE_TLS']=mailParam['mail']['tls']
mail = Mail(app)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/send-mail/')
def send_mail():
	try:
		#enter the recipients mail, here sender mail used as recipient.
		msg = Message("urgent",
		  sender=mailParam['mail']['username'],
		  recipients=[mailParam['mail']['username'],])
		msg.body = mailParam['mail']['message']
		mail.send(msg)
		return render_template('sendMassage.html')
	except Exception(e):
		return(str(e)) 
