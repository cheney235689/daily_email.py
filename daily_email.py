import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    from_addr = "your_email@gmail.com"
    to_addr = "recipient_email@example.com"
    password = "your_email_password"
    
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "每日報告"
    
    body = "這是今天的報告內容。"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
        print("郵件發送成功")
    except Exception as e:
        print(f"發送郵件失敗: {e}")

# 安排每天的任務
schedule.every().day.at("09:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)