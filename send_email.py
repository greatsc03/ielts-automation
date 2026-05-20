import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_ielts_email(html_content):
    """
    생성된 IELTS HTML 콘텐츠를 이메일로 전송합니다.
    """
    sender_email = "sangnom12@gmail.com"
    receiver_email = "sangchan.jo@samsung.com"
    
    # 이메일 앱 비밀번호는 환경변수에서 가져옵니다 (보안)
    password = os.environ.get("EMAIL_APP_PASSWORD")
    if not password:
        raise ValueError("EMAIL_APP_PASSWORD 환경 변수가 설정되지 않았습니다.")

    # 이메일 메시지 설정
    msg = MIMEMultipart("alternative")
    today_str = datetime.now().strftime("%Y-%m-%d")
    msg['Subject'] = f"[{today_str}] Daily IELTS General Training Reading Practice"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # HTML 내용을 이메일 본문에 첨부
    part = MIMEText(html_content, "html")
    msg.attach(part)

    # Gmail SMTP 서버를 통해 이메일 발송
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"이메일이 성공적으로 {receiver_email} 로 전송되었습니다!")
    except Exception as e:
        print(f"이메일 전송 중 오류 발생: {e}")

if __name__ == "__main__":
    # 로컬 테스트용
    dummy_html = "<h2>Test Email</h2><p>This is a test email.</p>"
    send_ielts_email(dummy_html)
