import logging
from preprocessing import clean_html, split_string ,extract_json_code
from bs4 import BeautifulSoup
import os
import requests
import tiktoken as tiktoken
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from dummyhtmldata import html
import json
from crew_utils import TestCrew


load_dotenv()
app = Flask(__name__)

CORS(app)

@app.route('/htmlagent',methods=['GET'])
def htmlagent():
    cl_html = clean_html(html)
    snippets = split_string(cl_html)
    print(len(snippets))
  
    all_test_flows = []

    # for snippet in snippets:
    #     crew = TestCrew(str(snippet)).kickoff_crew()
    #     test_flows_str = crew.kickoff()
    #     print(f"test_flows_str: {test_flows_str}")  # Debug line
    #     try:
    #         test_flows = json.loads(test_flows_str)
    #     except json.JSONDecodeError:
    #         # Split the string by the separators between the JSON objects and parse each one separately
    #         test_flows = [json.loads(part) for part in test_flows_str.split('}{') if part]
    #     all_test_flows.extend(test_flows)

    for snippet in snippets:
        crew = TestCrew(str(snippet)).kickoff_crew()
        test_flows_str = crew.kickoff()
        # print(type(test_flows_str))
        print(test_flows_str)
        test_flows_str=extract_json_code(test_flows_str)
        # print(type(test_flows_str))
        # print(len(test_flows_str))
        test_flows = json.loads(test_flows_str)
        # print(type(test_flows))
        print(test_flows)
        all_test_flows.extend(test_flows)
        
    print(all_test_flows)
    return jsonify({"message": "Success", "data": all_test_flows})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8086)








    


