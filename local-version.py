# This file is to test if your version of OI allows for Python scripts to be run with a local model

import sys

sys.path.insert(0, "/Users/mike/Code/open-interpreter")

from interpreter import interpreter

interpreter.offline = True
interpreter.llm.model = "ollama/dolphin-mixtral:8x7b-v2.6"
interpreter.llm.api_base = "http://localhost:11434"
interpreter.llm.context_window = 16000
interpreter.llm.max_tokens = 8000
interpreter.auto_run = True


def run(prompt):
    interpreter.chat(prompt)


run("how many files are on my desktop?")
