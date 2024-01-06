import smtplib
my_email = "axstest2023@gmail.com"

# Gmail doesn't let any application send an email, you must create/use a gmail app password
# Instructions for creating an app password can be found below
# https://support.google.com/accounts/answer/185833?hl=en 
password = "aivycehalywwpjno"

# Make a connection, use "with" to avoid having to close out the connection with a connection.close() at the end.
# To send an email from yahoo you would need to use smtp.mail.yahoo.com in the line below.
with smtplib.SMTP("smtp.gmail.com") as connection:

     # Start Transfer Layer Security (TLS).  Encrypts our email in case it is intercepted.
     connection.starttls()

     # Login
     connection.login(user=my_email, password=password) 

     # Send the email

     connection.sendmail(
                from_addr=my_email, 
                to_addrs="artsingletary@yahoo.com", 
                msg="Subject:Happy New Year\n\nHope you have a great year"
                )

