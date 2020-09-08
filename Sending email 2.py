import smtplib

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port   
session.starttls() #enable security This part needs not to be changed.

'''
with gmail, you have to change a seting in your google account to allow less secure apps.
Copy paseted form stack overflow:
In a nutshell, google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure",
so what you have to do is go to this link while you're logged in to your google account, and allow the access:

https://www.google.com/settings/security/lesssecureapps

/endpaste
apperently, google resets this switch after a while for security. I have not tried with IISERB account. They might disallow this entirely.
'''


session.login('maheshKNB@gmail.com', 'Password_in_single_quotes') #login with mail_id and password

session.sendmail('maheshKNB@gmail.com', # Sender
                 'abhijith16@iiserb.ac.in',# Reciver
                 'Subject: You have email! \n This is the body. \n\nSigned, Yours Truely.') #Subject \n Body

session.quit()
