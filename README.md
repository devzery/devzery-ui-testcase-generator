# [![N|Solid](https://static.wixstatic.com/media/8490f3_c39f7a1fe2684c5181ac6b59efc252b0~mv2.png/v1/fill/w_89,h_90,al_c,lg_1,q_85,enc_auto/8490f3_c39f7a1fe2684c5181ac6b59efc252b0~mv2.png)](https://www.devzery.com/) 

# UI Test-Case Generation Tool


## Outline

This tool helps create well-defined and well-structured functional testcases based on the provided HTML content. This tool uses a crew of AI-agents to interpret the recieved HTML data, percieve UI components and features, understands, uses, and then curates a list of well-defined testcases. 

This tool is built using Flask and communicates with the CrewAI workload to manage cooperation across an agentic crew. Also it uses a variety of additional libraries, such as BeautifulSoup, to parse and clean provided HTML content.


## Features

- **Compatibility** : This tool is compatible with any of the **Langchain Supported Models**

- **Identification of Functionality** : As per the structure of the provided HTML, the tool understands the expected usecase and also keeping the context of webapp intact and even considers the possible user-interactions and prospects.

- **TestCase Generation** : Based upon all the different componets of HTML corpus comes a set of well-defined fucntional testcases.The AI agents understand crucial points like navigational flows, edgecases, user auths and access, data manipulation operations and dynamic content handling.

- **Handling for Roles and Permissions** : The tool considers into account the user's roles and various levels of approval and access.

- **Edge Cases** : The boundary conditions and potential edgecases are percieved.

- **Output**: A JSON schema is defined as illustrated. The final output consists a well-structrued JSON following the shown schema.

```json
    {
        "test_cases": [
            {
                "test_case_description": "Test case description",
                "dependencies": "List of dependencies",
                "test_steps": "Steps to execute the test case",
                "expected_result": "Expected result of the test case"
            },
            
        ]
    }, 
```


## Getting Started

To use the tool follow these steps:

1. Clone The Repository

2. Use `pip install -r requirements.txt` to install the required dependencies.


3. Create a Virtual Environment

- Navigate to your project directory where you want to create the virtual environment and Open a terminal (or command prompt).

- **Run the following command** to create the virtual environment:

    ```bash
    python -m venv myenv
    ```

    Replace `myenv` with your preferred name for the virtual environment.

 #### Activate the Virtual Environment

- On Windows
Run the following command:

```bash
myenv\Scripts\activate
```
- On macOS and Linux
Run the following command:

```bash
source myenv/bin/activate
```


4. This tool leverages use of LangChain. Using LangChain this tool is compatible with **any language model** that Langchain supports , for more information regarding LangChain please refer to the following documentation

**(https://python.langchain.com/v0.2/docs/introduction/)**


- After the dependencies are installed, set the required environment variables as per the Langchain Documentation.

- We've used **OpenAI gpt-4-0125-preview** as the default LLM for the tool. If you would like to use the same, then set the OpenAI API key as environment variable:
OPENAI_API_KEY : "Your OpenAI API key" 


5. To use any other LangChain model, instantiate a variable as per the langchain documentation for that model and pass this variable as a parameter to `TestCrew` Class Object in `app.py` file as shown below


```python
#....Continued code 
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4-0125-preview",
    temperature=0,
    max_tokens=None,
)
@app.route('/htmlagent',methods=['POST'])

    #.....Rest of the code remains the same
    

    for snippet in snippets:
        crew = TestCrew(str(snippet),llm=llm).kickoff_crew() #Pass your llm here
        
        
    #Rest of the code remains the same.......
```


Here is how you can use **ChatAnthropic LLM** for the application(https://python.langchain.com/v0.2/docs/integrations/platforms/anthropic/):


- Run `pip install -U langchain-anthropic` To install dependencies (Please refer Langchain Docs).

- Set up your necessary environment variables :
   - `ANTHROPIC_API_KEY`: Your Anthropic API key

- In your `app.py` file 

```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model='claude-3-opus-20240229')

#Code Continued....
```

- Pass `llm` as a parameter in `TestCrew` Class Object :

```python
#....Continued code 
@app.route('/htmlagent',methods=['POST'])

    #.....Rest of the code remains the same
    

    for snippet in snippets:
        crew = TestCrew(str(snippet),llm=llm).kickoff_crew() #Pass your llm here
        
        
    #Rest of the code remains the same.......
```

6. Run the Flask Application Server 

7. Hit `/htmlagent` endpoint using a POST method.

8. The HTML data must be sent in the following JSON format with the HTML stringified.

 ```json
 {
    "html": "Your Stringified HTML content"
 }
 ```

## Contributing To the Project

Being an opensource project, all your contributions are highly anticipated ! If you take interest in this and encounter any issues or have further suggestions for improvements, please do open an issue or submit a Pull Request. Do make sure to follow the Project's coding conventions.

To contribute to this project,

1. Fork the repositories
2. Make a distinct branch for the feature or issue fixes.
3. Make your modifications and commit them.
4. Publish your modifications to your forked repository.
5. Submit a new pull request to the original repository.