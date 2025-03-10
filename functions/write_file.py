def write_content_to_file(content, filename, extension):
    with open('.\\made_by_ai\\' + filename + extension, "a") as f:
        f.write(content + '\n')  # Append newline for readability
