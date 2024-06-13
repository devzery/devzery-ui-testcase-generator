# [![N|Solid](https://static.wixstatic.com/media/8490f3_c39f7a1fe2684c5181ac6b59efc252b0~mv2.png/v1/fill/w_89,h_90,al_c,lg_1,q_85,enc_auto/8490f3_c39f7a1fe2684c5181ac6b59efc252b0~mv2.png)](https://www.devzery.com/) 

# UI Test-Case Generation Tool


## Outline

This tool helps create well-defined and well-structured functional testcases based on HTML content. This app uses a crew of AI-agents to interpret the recieved HTML data, percieve UI components and features, understands uses, and then curates a list of well-defined testcases. 

This application is built using Flask and communicates with the CrewAI workload to manage cooperation across an agentic crew. Also it uses a variety of additional libraries, such as BeautifulSoup, to parse HTML and eliminate unwanted HTML elements such as svg, style, and script.


## Features

- **Compatibility** : This application is compatible with any of the **Langchain Models**

- **Identification of Functionality** : As per the structure of the provided HTML, the tool understands the expected usecase and also keeping the context of webpage/webapp intact and even considers the possible user-interactions and prospects.

- **TestCase Generation** : Based upon all the different componets of HTML corpus comes a set of well-defined fucntional testcases. The app also keeps crucial points like navigational flows, edgecases, user auths and access, data manipulation opeartions and dynamic content handling.

- **Handling for Roles and Permissions** : The app considers into account the user's roles and various levels of approval and access which are very well capable of affecting UI's behaviour on interaction.

- **Edge Cases** : The boundary conditions, Potential edgecases and alternative scenarios are percieved and are also listed in testcases.

- **Output**: A JSON schema is defined as illustrated. The final output consists a well-structrued JSON following the shown schema. This helps in combining further with other testing frameworks and tools.

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


4. This application Leverages use of LangChain. Using LangChain this tool is compatible to **any Language model** that Langchain supports , You can install langchain by referring the following documentation for LangChain

**(https://python.langchain.com/v0.2/docs/how_to/installation/)**


- After your dependencies are installed you must set the required environment variables as per the Langchain Documentation.

- To initialise the LLMs using Langchain please refer **Langchain Dcoumentation**

- We've used OpenAI as the default LLM for the tool. If you would like to use the same, then set the OpenAI API key as environment variable:
OPENAI_API_KEY : "Your OpenAI API key"

As mentioned this app is configured to use **OpenAI with gpt-4-0125-preview** as a default model. To use and ovevrride a model diffrent than default you have to set the expected environment for that model provider.



5. To use any other langchain model which is different than the Default model You have to instantiate `llm` variable as per the langchain documentation for that model and pass this `llm` variable as a parameter to `TestCrew` Class Object

- Here is an Example on how you can Instantiate a Custom OpenAI LLM on default one. This customises the default one as per parameters.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    max_tokens=None,
)
```

we need to pass this `llm` variable as a parameter in `crew = TestCrew(str(snippet),llm=llm).kickoff_crew()`



- Now if your required model is different than the one that is default, you must refer from the official Langchain Documentation on How to install the required dependencies, How to set the environment variables for that particular model provider and understand How that particualr model is instatiated using Langchain for the required model provider to expose the model to `llm` variable.


For example Here is how you can use **ChatAnthropic LLM** for the application:

- Run `pip install -U langchain-anthropic` To install dependencies (Please refer Langchain Docs).

- Set up your necessary environment variables that are expected :
   - `ANTHROPIC_API_KEY`: Your Anthropic API key

- After your environment is set , with required keys , In `app.py` This is how you define the `llm` as language model.

```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model='claude-3-opus-20240229')

#Code Continued....
```

- And pass `llm` as a parameter in `TestCrew` class Object something like this :

```python
#....Continued code 
@app.route('/htmlagent',methods=['POST'])

    #.....Rest of the code remains the same
    

    for snippet in snippets:
        crew = TestCrew(str(snippet),llm=llm).kickoff_crew() #Pass your llm here
        
        
    #Rest of the code remains the same.......
```



**Please Consider Reffering to Langchain Documentation for more information On how to install Langchain as well as How to define and expose LLM's using Langchain for whichever LLM you desire.**

**(https://python.langchain.com/v0.2/docs/how_to/installation/)**



6. Run the Flask Application Server (i.e) run `app.py` and Send a POST request to the server host url and `/htmlagent` endpoint.

7. The HTML data must be sent as a JSON request payload and the HTML data must be stringified initially.The following is the expected JSON Schema for the request paylaod:


 ```json
 {
    "html": "Your Stringified HTML content"
 }
 ```

## Contributing To the Project

Being an opensource project, all your contributions are highly anticipated ! If you take interest in this and encounter any issues or have further suggestions for improvements, please do open an issue or submit a Pull Request. Do make sure to follow the Project's coding conventions and guidelines.

To contribute to this project,

1. Fork the repositories
2. Make a distinct branch for the feature or issue fixes.
3. Make your modifications and commit them.
4. Publish your modifications to your forked repository.
5. Submit a new pull request to the original repository.