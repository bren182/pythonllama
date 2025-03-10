import ollama
from functions import write_file
import logging

logging.basicConfig(level=logging.DEBUG)

def main(prompt):
    logging.debug("Starting Ollama chat stream")
    response_stream = ollama.chat(
        'llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}],
        tools=[
            write_file.write_content_to_file,
        ],
        stream=True
    )

    full_response = ""
    tool_calls = []

    try:
        for chunk in response_stream:
            logging.debug(f"Received chunk: {chunk}")
            if 'message' in chunk:
                if 'content' in chunk['message']:
                    full_response += chunk['message']['content']
                if 'tool_calls' in chunk['message']:
                    tool_calls.extend(chunk['message']['tool_calls'])

    except Exception as e:
        logging.error(f"An error occurred during streaming: {e}")
        return full_response

    logging.debug(f"Full response collected: {full_response}")
    logging.debug(f"Tool calls collected: {tool_calls}")

    # Function mapping
    available_functions = {
        'write_content_to_file': write_file.write_content_to_file,
    }

    for tool in tool_calls:
        function_name = tool['function']['name']
        function_to_call = available_functions.get(function_name)

        if function_to_call:
            arguments = tool['function']['arguments']
            logging.debug(f'Running function: {function_name} with arguments {arguments}')
            
            try:
                result = function_to_call(**arguments)
                logging.debug(f'result was: {result}')
            except Exception as e:
                logging.error(f"An error occurred while calling the function {function_name}: {e}")
        else:
            logging.warning(f'Function not found: {function_name}')
    
    return full_response