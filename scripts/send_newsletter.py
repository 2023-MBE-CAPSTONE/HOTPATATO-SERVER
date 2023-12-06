import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import smtplib
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from dynamodb.users import Users

load_dotenv(verbose=True)

def connect_smtp_server() -> SMTP_SSL:
    gmail_smtp = "smtp.gmail.com"  
    gmail_port = 465 
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
    return smtp


def send_newsletter(
        smtp: SMTP_SSL,
        receiver_email: str,
        html_content
    ):
    hotpotato_gmail_account = os.getenv("HOTPOTATO_GMAIL_ACCOUNT")
    hotpotato_gmail_app_password = os.getenv("HOTPOTATO_GMAIL_APP_PASSWORD")
    smtp.login(hotpotato_gmail_account, hotpotato_gmail_app_password)

    message = MIMEMultipart()
    message["Subject"] = f"노란봉투법 논쟁: 노동자 보호 vs 기업 부담, 양날의 검"  
    message['From'] = hotpotato_gmail_account
    message['To'] = receiver_email

    message.attach(MIMEText(html_content, 'html'))
    smtp.sendmail(hotpotato_gmail_account, receiver_email, message.as_string())
    smtp.quit()


if __name__ == "__main__":

    smtp_server = connect_smtp_server()
    user = Users()
    email_list = user.get_user_email_list()

    with open('./templates/sample_newsletter.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    for email in email_list:
        send_newsletter(smtp_server,email,html_content)

