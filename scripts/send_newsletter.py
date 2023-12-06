import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import smtplib
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

from dynamodb.users import Users
from dynamodb.generated_newsletter import GeneratedNewsletters


load_dotenv(verbose=True)

def connect_smtp_server() -> SMTP_SSL:
    gmail_smtp = "smtp.gmail.com"  
    gmail_port = 465 
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
    return smtp


def send_email_using_html(
        smtp: SMTP_SSL,
        receiver_email: str,
        title: str,
        html_content: str
    ):
    hotpotato_gmail_account = os.getenv("HOTPOTATO_GMAIL_ACCOUNT")
    hotpotato_gmail_app_password = os.getenv("HOTPOTATO_GMAIL_APP_PASSWORD")
    smtp.login(hotpotato_gmail_account, hotpotato_gmail_app_password)

    message = MIMEMultipart()
    message["Subject"] = title
    message['From'] = hotpotato_gmail_account
    message['To'] = receiver_email

    message.attach(MIMEText(html_content, 'html'))
    smtp.sendmail(hotpotato_gmail_account, receiver_email, message.as_string())

def send_hot_potato(user_email_list: list, title_html_list: list):
    for email in email_list:
        for title,html in title_html_list:
            send_email_using_html(smtp_server,email,title,html)

if __name__ == "__main__":

    user = Users()
    email_list = user.get_user_email_list()

    gm = GeneratedNewsletters()
    title_html_list = gm.get_generated_newsletter_list("20231205")
    
    smtp_server = connect_smtp_server()
    send_hot_potato(email_list,title_html_list)
    smtp_server.quit()