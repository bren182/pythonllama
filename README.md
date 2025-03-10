# Introduction

LLM agent to demo basic function-calling, in this project we want to prompt an LLM to _DO_ stuff instead of just spitting out stuff. 

We can ask the program to write anything to a file!

## PyOllama agent with function calling

This project requires at least `Python 3.13.1` and a local Ollama instance running on your machine. 

Use `llama3.2:3b` LLM model to perform tasks. 

Download ollama [here](https://ollama.com/download)

Download Python [here](https://www.python.org/downloads/)

## Example Usage 

### Running from terminal  
![run_program](https://github.com/user-attachments/assets/da9767b8-f503-4bc4-9d75-183e9cee9fde)

### Output of terminal

![output](https://github.com/user-attachments/assets/d26cd561-b5f8-4a76-89c0-1d2d6a3a5327)


## Instructions

Make sure you have the `llama3.2:3b` model installed in your local Ollama instance. 
`ollama list` will output all available models. 

If you do not see `llama3.2:3b`, then run `ollama run llama3.2:3b` 

Now you can start using the program `main.py`!
1. Write a python script... `python main.py "write a python script which adds two numbers, ask the user for input for both numbers" "llama"`
2. Write me a joke... `python main.py "write a joke" "llama"`

- The main.py takes two arguments: 
    - The prompt
    - The model we are running as an "agent"
 



Currently function calling only built for the Ollama model (`llama3.2:3b` used). 

The program will output any written files to a folder called `made_by_ai`. 

## Known bugs

When asking for a simple joke, sometimes the punch-line gets left out. 

Sometimes the output of writing to a file gets cut off. Need to figure out why this happens and a strategy to prevent the program from finishing execution before all content has been written. 
