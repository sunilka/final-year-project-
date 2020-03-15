import email
import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login('wingsoffirew@gmail.com','wingswings')
mail.list()
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print ('Processing ')
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_bytes(response_part[1])

            # print (original['From'])
            # print (original['Subject'])
             raw_email = data[0][1]
             raw_email_string = raw_email.decode('utf-8')
             email_message = email.message_from_string(raw_email_string)
             for part in email_message.walk():
                        if (part.get_content_type() == "text/plain"): # ignore attachments/html
                              body = part.get_payload(decode=True)
                              save_string = str(r"C:\Users\Shruthi\Desktop\new" + str('richboy') + ".txt" )
                              myfile = open(save_string, 'a')
                              myfile.write(original['From']+'\n')
                              myfile.write(original['Subject']+'\n')            
                              myfile.write(body.decode('utf-8'))
                              myfile.write('**********\n')
                              myfile.close()
                        else:
                              continue

             typ, data = mail.store(num,'+FLAGS','\\Seen')

print (n)