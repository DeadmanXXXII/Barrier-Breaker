import language_tool_python

def correct_grammar(text, lang="en-US"):
    tool = language_tool_python.LanguageTool(lang)
    matches = tool.check(text)
    return language_tool_python.utils.correct(text, matches)
