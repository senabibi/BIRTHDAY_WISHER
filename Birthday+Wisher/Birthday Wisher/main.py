import smtplib

my_email="bitirgensena@gmail.com"
password="abcd1234()"
with smtplib.SMTP("smtp.gmail.com") as connection:


    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="bitirgensena@gmail.com",
                        msg="Subject:Hello\n\n This is a random message.")
   