import os
from google import genai

def generate_ielts_reading():
    """
    Gemini API를 사용하여 IELTS General Training Reading 문제 1세트를 생성합니다.
    """
    # 환경 변수에서 API 키를 가져옵니다.
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")

    client = genai.Client(api_key=api_key)

    prompt = """
    You are an expert IELTS test creator.
    Please generate one complete set of IELTS General Training Reading test materials.

    Requirements:
    1. Passage: Create an original, realistic reading passage suitable for IELTS General Training (Section 1, 2, or 3). 
       The topic should be related to everyday life, work, or general interest (approx. 500-800 words).
    2. Questions: Create 13-14 questions based on the passage. Mix at least two different question types from the following:
       - True/False/Not Given
       - Multiple Choice
       - Matching Headings
       - Sentence Completion
       - Matching Information
    3. Answers: Provide the correct answer key at the very bottom, clearly separated from the questions.

    Format the output strictly in HTML so that it can be directly embedded in an email body.
    Use basic HTML tags like <h1>, <h2>, <p>, <b>, <br>, <ul>, <li>, etc.
    Do not include markdown code block syntax (like ```html), just output the raw HTML string.
    Ensure the design is clean and easy to read.

    Example structure:
    <h2>IELTS General Training Reading Practice</h2>
    <h3>Passage Title</h3>
    <p>[Passage content...]</p>
    <hr>
    <h3>Questions 1-7</h3>
    <p><b>Instructions...</b></p>
    [Questions...]
    <hr>
    <h3>Questions 8-13</h3>
    <p><b>Instructions...</b></p>
    [Questions...]
    <br><br><br>
    <hr>
    <h3>Answer Key</h3>
    [Answers...]
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        # Markdown 포맷으로 응답이 올 경우를 대비해 앞뒤의 ```html 과 ``` 를 제거
        html_content = response.text.strip()
        if html_content.startswith("```html"):
            html_content = html_content[7:]
        if html_content.startswith("```"):
            html_content = html_content[3:]
        if html_content.endswith("```"):
            html_content = html_content[:-3]
            
        return html_content.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        return f"<h2>Error generating IELTS content</h2><p>{e}</p>"

if __name__ == "__main__":
    # 로컬 테스트용
    print(generate_ielts_reading())
