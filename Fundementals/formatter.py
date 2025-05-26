class UpperCaseFormatter:
    def format_text(self,text):
        return text.upper()

class LowerCaseFormatter:
    def format_text(self,text):
        return text.lower()

class TitleCaseFormatter:
    def format_text(self,text):
        return text.title()

def apply_formatters(text, formatters):
    for formatter in formatters:
        text = formatter.format_text(text)
    return text
