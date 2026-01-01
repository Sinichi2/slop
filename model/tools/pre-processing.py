import base64
from langchain.messages import HumanMessage



class preprocessing:
    #Processing 
    def process_image(image_path): 
        with open(image_path, 'r') as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        
        message = HumanMessage(content = [
            {        {"type": "text", "text": "Extract all events from this screenshot."},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}}
        ])

        return aggregator_agent.invoke([message])


    def process_pdf(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = base64.b64encode(f.read()).decode("utf-8")
        
        message = HumanMessage(content=[
            {"type": "text", "text": "Extract all events from this document."},
            {"type": "document", "data": pdf_data, "media_type": "application/pdf"}
        ])
        return aggregator_agent.invoke([message])