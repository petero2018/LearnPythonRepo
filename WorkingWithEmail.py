import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()
msg = "Hello"

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("kiralymatyas888@gmail.com", password)
    server.sendmail('kiralymatyas888@gmail.com','kiralymatyas888@gmail.com',msg)

