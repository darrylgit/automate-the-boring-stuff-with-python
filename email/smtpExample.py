import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()

conn.starttls()

print(conn.login('daniel.j.wagener@gmail.com', '<password>'))

conn.sendmail('daniel.j.wagener@gmail.com', 'daniel.j.wagener@gmail.com',
              'Subject: Hi me\n\nDear Daniel, \nWell, here ya go')

conn.quit()
