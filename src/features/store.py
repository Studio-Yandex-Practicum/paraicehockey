# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib


# Нужно поменять message['From'] на адрес реальной почты проекта, 
# в password записать пароль от нее
# также в строке 16 указать сервер почты для smtp(например smtp.yandex.ru)
# def send_mail(user_email):
#     message = MIMEMultipart()
#     message_text = 'Спасибо за Ваш заказ! Мы уже начали работать над ним.'
#     password = 'your_password'
#     message['From'] = 'our_address'
#     message['To'] = user_email
#     message['Subject'] = 'NO-Reply--Заказ paraicehockey'
#     message.attach(MIMEText(message_text, 'plain'))
#     email = smtplib.SMTP('smtp.gmail.com: 587')
#     email.starttls()
#     email.login(message['From'], password)
#     email.sendmail(message['From'], message['To'], message.as_string())
#     email.quit()
