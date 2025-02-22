import nltk
from nltk.tokenize import sent_tokenize
from transformers import pipeline

class TextAnalyzer:
    def __init__(self):
        nltk.download('punkt', quiet=True)
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def analyze_and_respond(self, text):
        # Простое определение типа входного текста
        if '?' in text:
            return self.answer_question(text)
        else:
            return self.summarize(text)

    def summarize(self, text):
        MAX_RESPONSE_LENGTH = 200  # или любое другое значение
        summary = self.summarizer(text, max_length=MAX_RESPONSE_LENGTH, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def answer_question(self, question):
        # Здесь должен быть контекст для ответа на вопрос
        # В реальном приложении это может быть база знаний или предыдущий контекст разговора
        context = "Это пример контекста для ответа на вопросы. " \
                  "Здесь может быть информация о текущей теме разговора или общие знания."

        answer = self.qa_model(question=question, context=context)
        return answer['answer']

if __name__ == "__main__":
    analyzer = TextAnalyzer()
    test_text = "Искусственный интеллект становится все более важным в современном мире. Он применяется в различных областях, от медицины до финансов."
    print("Тестовый анализ:", analyzer.analyze_and_respond(test_text))

    test_question = "Какие области применения ИИ упомянуты?"
    print("Тестовый ответ на вопрос:", analyzer.analyze_and_respond(test_question))
