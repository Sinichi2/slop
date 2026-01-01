FROM python:3.14-latest 

RUN pip install fastmcp 

COPY /model/main_mcp.py .

# Running the server 
CMD ['python', "main_mcp.py", "run", "--transport", "sse"]

