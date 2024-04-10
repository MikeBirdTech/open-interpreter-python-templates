from interpreter import interpreter

interpreter.offline = True
interpreter.llm.api_base = "http://localhost:11434"
interpreter.llm.model = "ollama/dolphin-mixtral:8x7b-v2.6"
interpreter.llm.context_window = 16000
interpreter.llm.max_tokens = 8000
interpreter.auto_run = True


def run(prompt):
    interpreter.chat(prompt)


run("how many files are on my desktop?")
