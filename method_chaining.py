# ===========================================
# 메서드의 반환 타입에 따라 쓸 수 있는 메서드가 달라진다
# ===========================================


class TextBox:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_text(cls, text):
        """클래스 메서드: TextBox 객체를 만들어서 반환"""
        return cls(text)

    def get_words(self):
        """문자열을 쪼개서 리스트로 반환"""
        return self.text.split()

    def get_first_word(self):
        """첫 번째 단어를 문자열로 반환"""
        return self.text.split()[0]


box = TextBox.from_text("hello world python")


# ── 1) list를 반환하는 메서드 → list의 기능을 쓸 수 있다 ──

result = box.get_words()
print(result)        # ['hello', 'world', 'python']
print(type(result))  # <class 'list'>

print(result[0])           # hello     ← 인덱싱 가능
print(result.count("hello"))  # 1     ← list의 메서드 사용 가능
# result.upper()  # 에러! list에는 upper()가 없다
print()


# ── 2) str을 반환하는 메서드 → str의 기능을 쓸 수 있다 ──

result = box.get_first_word()
print(result)        # hello
print(type(result))  # <class 'str'>

print(result.upper())            # HELLO   ← str의 메서드 사용 가능
print(result.replace("h", "H"))  # Hello   ← str의 메서드 사용 가능
# result[0:] 같은 슬라이싱도 가능
# result.count("hello") 도 가능 (str에도 count가 있으니까)
# result.append("!") 는 에러! str에는 append()가 없다
