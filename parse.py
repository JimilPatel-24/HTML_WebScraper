import os  
from langchain_core.messages import HumanMessage        
from langchain_google_genai import ChatGoogleGenerativeAI

TOKEN = os.getenv("GEMINI_API_TOKEN")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=TOKEN) 



def parse_with_gemini(dom_chunks, parse_desc):
    results = []
    for i, chunk in enumerate(dom_chunks, 1):
        prompt = (
            "You are tasked with extracting specific information from the following text content: {dom_content}. "
            "Please follow these instructions carefully: \n\n"
            f"Extract ONLY: {parse_desc}\n"
            f"Text context: {chunk}\n"
            "Constraint: Output data only. No intro, no conversational filler.Empty Response:If no information matches the description, return an empty string ('')."
        )
        try:
            response = model.invoke([HumanMessage(content=prompt)])
            content = response.content
            if isinstance(content, list):
                content = " ".join([part if isinstance(part, str) else str(part.get("text", "")) for part in content])
            parsed_content = str(content).strip()
            
            if parsed_content:
                results.append(parsed_content)
                print(f"Successfully parsed batch {i}/{len(dom_chunks)}")
            else:
                print(f"Batch {i}: No matching data found.")

        except Exception as e:
            print(f"Error parsing batch {i}: {e}")
            
    return "\n".join(results)