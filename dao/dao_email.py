import logging
import smtplib, ssl

class DaoEmail:
    port: int = 587  # For SSL
    smtp_server: str = "smtp.gmail.com"
    password: str = ""
    sender_email: str
    def __init__(self):
        logging.info("Initializing Email DAO")
        self.port = 587
        self.smtp_server = "smtp.gmail.com"
        self.password = "*****************"
        self.sender_email = "disttimetracker@gmail.com"

    def send(self, to_email: str, title: str, message: str):
        logging.info("Sending email !!!!!!!!!!!!!!!!!!!!!!!!")
        context = ssl.create_default_context()
        # Try to log in to server and send email
        server = None
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.sender_email, self.password)
            # TODO: Send email here
            server.sendmail(self.sender_email, to_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()

