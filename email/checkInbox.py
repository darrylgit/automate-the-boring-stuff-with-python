import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('daniel.j.wagener@gmail.com', '<password>')
print(conn.select_folder('INBOX', readonly=True))

UIDs = conn.search(['SINCE', '10-Mar-2020'])

rawMessage = conn.fetch([38642], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[38642][b'BODY[]'])

print(message.get_subject())

print(message.text_part.get_payload().decode('UTF-8'))
