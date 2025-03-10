
import sys
import agents.ollama_agent
from test import my_test as tests


def main(prompt, model):
    myfunc = tests.a_test
    print(f'what is my func? {myfunc}')
    response = ""
    if model == "llama":
        response = agents.ollama_agent.main(prompt)
    return print(f"Response finished! {response}")

if __name__ == '__main__':
    if sys.argv[2] == "llama":
        main(sys.argv[1], "llama")
    else:
        print(f'unsupported model: "{sys.argv[2]}"')

