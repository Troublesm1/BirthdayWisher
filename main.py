import smtplib

my_email = "xxx@gmail.com"
password = "xxx"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="xxx@yahoo.com",
        msg="Subject: Test\n\nThe body of the email"
    )




# ---------- Hotmail -------------
# my_email = "myemailhere.com"
# connection = smtplib.SMTP("smtp.live.com")

# ---------- Yahoo -------------
# my_email = "myemailhere.com"
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
