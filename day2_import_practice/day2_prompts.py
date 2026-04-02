# prompts.py — 프롬프트 생성 함수를 모아놓은 파일

def make_prompt(role, topic):
    return f"당신은 {role}입니다. {topic}에 대해 설명해주세요."


def translate_prompt(text, source_lang, target_lang):
    return f"{source_lang}에서 {target_lang}로 번역해주세요: {text}"
