
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("thanhhuynhdeo@gmail.com","Thanh123")
msg = "Hello friends"
for i in range(5):
    if i<5:
        server.sendmail("thanhhuynhdeo@gmail.com","quydao360@gmail.com",msg)
        i+=1
server.quit()