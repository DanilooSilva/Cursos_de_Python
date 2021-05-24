from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open(r'aula136\template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_mgn = template.substitute(nome="Danilo Gomes", data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Danilo Gomes'
msg['to'] = 'danilo_silva640@hotmail.com'
msg['subject'] = 'Atenção: este é um e-amil de teste'

corpo = MIMEText(corpo_mgn, 'html')
msg.attach(corpo)

with open(r'aula136\20210107_131456.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('E-mail não enviado')
        print(f'erro: {e}')