from generate_ielts import generate_ielts_reading
from send_email import send_ielts_email

def main():
    print("IELTS 문제 생성을 시작합니다...")
    html_content = generate_ielts_reading()
    
    if "Error generating IELTS content" in html_content:
        print("문제 생성에 실패했습니다. 이메일을 전송하지 않습니다.")
        return
        
    print("이메일 전송을 시작합니다...")
    send_ielts_email(html_content)
    print("모든 작업이 완료되었습니다.")

if __name__ == "__main__":
    main()
