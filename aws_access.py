import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendUpdates(user, contestant):

    try:

        # Replace sender@example.com with your "From" address. 
        # This address must be verified.
        SENDER = 'cfrankingupdate@gmail.com'  
        SENDERNAME = 'lukesfather'

        # Replace smtp_username with your Amazon SES SMTP user name.
        USERNAME_SMTP = "AKIA4NPSV35DEI4DB7MT"

        # Replace smtp_password with your Amazon SES SMTP password.
        PASSWORD_SMTP = "BN9Z780kf9cxAv1DnkhSQ5xXzAlKhueUCbDaZS2nIAlz"

        # If you're using Amazon SES in an AWS Region other than US West (Oregon), 
        # replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP  
        # endpoint in the appropriate region.
        HOST = "email-smtp.us-east-1.amazonaws.com"
        PORT = 587

        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)

        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        RECIPIENT  = user['useremail']

        

        # The subject line of the email.
        SUBJECT = 'Codeforces Rating Update!'

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = ("Hi " 
                    # user['username']
                    "!\n"
                    "Your new rating is : "
                    )

        new_rating = contestant['newRating']
        name = user['username']

        message = 'Hello ' + name + '! your new rating is ' + str(new_rating);
        print(message)


        # The HTML body of the email.
        BODY_HTML = """<html>
        <head></head>
        <body>
        <h1>Hi, Name!</h1>
        <p>Congratulations / Better luck next time! <br>
        Your new rating at Codeforces is : 
        </p>
        </body>
        </html>
                    """

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = SUBJECT
        msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
        msg['To'] = RECIPIENT
        # Comment or delete the next line if you are not using a configuration set
        # msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(message, 'plain')
        part2 = MIMEText(BODY_HTML, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        # msg.attach(part2)

        # Try to send the message.
        try:  
            server.sendmail(SENDER, RECIPIENT, msg.as_string())
            # server.sendmail(SENDER, RECIPIENT, msg.as_string())
        # Display an error message if something goes wrong.
        except Exception as e:
            print ("Error: ", e)
        else:
            print ("Email sent to " + user['username'])
        
        server.close()

    except Exception as e:
        print ("Error: ", e)
    else:
        print ("All Set!")