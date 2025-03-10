# Introduction

LLM agent to demo basic function-calling, in this project we want to prompt an LLM to _DO_ stuff instead of just spitting out stuff. 

We can ask the program to write anything to a file!

## PyOllama agent with function calling'

This project requires at least `Python 3.13.1` and a local Ollama instance running on your machine. 

Use `llama3.2:3b` LLM model to perform tasks. 

Download ollama [here](https://ollama.com/download)

Download Python here

## Example Usage 

`python main.py "write a python script which adds two numbers, ask the user for input for both numbers" "llama"`

- The main.py takes two arguments: 
    - The prompt
    - The model we are running as an "agent"

Currently function calling only built for the Ollama model (`llama3.2:3b` used). 

The program will output any written files to a folder called `made_by_ai`. 
