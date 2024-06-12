from preprocessing import clean_html, split_string ,extract_json_code
import tiktoken as tiktoken
from flask import Flask, jsonify ,request
from dotenv import load_dotenv
from flask_cors import CORS
import json
import os
from langchain_openai import AzureChatOpenAI
from crew_utils import TestCrew


load_dotenv()
app = Flask(__name__)

CORS(app)

llm = AzureChatOpenAI(
    openai_api_version=os.getenv("openai_api_version"),
    azure_deployment=os.getenv("DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_type="azure",
)

@app.route('/htmlagent',methods=['POST'])
def htmlagent():
    all_test_flows = []
    request_data = request.get_json()  
    if request_data and 'html' in request_data:
        html_str = request_data['html']  
    else:
        return jsonify({"error": "Missing 'html' key in the request payload"}), 400
    
    cl_html = clean_html(html_str)
    snippets = split_string(cl_html)
    for snippet in snippets:
        crew = TestCrew(str(snippet),llm=llm).kickoff_crew()
        test_flows_str = crew.kickoff()
        test_flows_str=extract_json_code(test_flows_str)
        test_flows = json.loads(test_flows_str)
        all_test_flows.extend(test_flows)
        
    print(all_test_flows)
    return jsonify({"message": "Success", "data": all_test_flows})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8086)








    


