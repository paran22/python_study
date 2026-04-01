# 1차시_예제.py
# 이 파일은 터미널에서 python 1차시_예제.py 로 실행합니다
# 위에서 아래로 전체가 한 번에 실행됩니다

# --- 변수 ---
name = "가은"
topic = "AI 에이전트"
language = "한국어"

# --- f-string ---
message = f"{name}님, {topic}에 오신 것을 환영합니다!"
print(message)

# --- 함수 ---
def make_prompt(role, topic, language, style):
    prompt = f"""
당신은 {role}입니다.
{topic}에 대해 {language}로 {style} 설명해주세요.
"""
    return prompt

result = make_prompt("IT 전문가", "인공지능", "한국어", "쉽고 친절하게")
print(result)
