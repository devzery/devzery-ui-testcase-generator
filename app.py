from src.preprocessing import clean_html, split_string ,extract_json_code
from flask import Flask, jsonify ,request
from dotenv import load_dotenv
from flask_cors import CORS
import json
from src.crew_utils import TestCrew


load_dotenv()
app = Flask(__name__)

CORS(app)


@app.route('/htmlagent',methods=['POST'])
def htmlagent():

    try:
        all_tests = []
        request_data = request.get_json()
        if request_data and 'html' in request_data:
            html_str = request_data['html']
        else:
            return jsonify({"error": "Missing 'html' key in the request payload"}), 400

        cl_html = clean_html(html_str)
        snippets = split_string(cl_html)
        for snippet in snippets:
            crew = TestCrew(str(snippet)).kickoff_crew()
            test_flows_str = crew.kickoff()
            test_flows_str=extract_json_code(test_flows_str)
            test_flows = json.loads(test_flows_str)
            for testcase in test_flows['test_cases']:
                all_tests.append(testcase)



        return jsonify({"message": "Success", "data": all_tests})

    except Exception as e:
        return jsonify(({"message":"error", "data": e}))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)








    


