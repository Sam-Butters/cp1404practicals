"""
CP1404 Prac06 - Languages
Sam Butters
Time started: 12:58
Time finished: 13:31
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [python, ruby, visual_basic]
for language in languages:
    if language.is_dynamic():
        print(language.name)
