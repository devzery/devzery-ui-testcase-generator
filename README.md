# UI Test Case Generation Tool

## Overview
This project is designed to generate comprehensive functional test cases for HTML content. It leverages natural language processing and a team of AI agents to analyze the provided HTML, identify key components, functionalities, and potential user interactions, and generate a set of well-structured test cases.

The application is created with Flask and interfaces with the Crew AI system to manage collaboration across AI agents. It also makes use of numerous libraries, including Beautiful Soup for HTML parsing and for cleaning undesired HTML elements like svg , style and script.

## Features

- **HTML Analysis**: The application can analyze HTML content and identify key elements such as links, buttons, forms, dropdowns, navigation menus, popups, tooltips, accordions, tabs, and other UI components.

- **Functionality Identification**: Based on the HTML structure, the system identifies the purpose and context of the web page or application, as well as the key functionalities and potential user interactions.

- **Test Case Generation**: The application generates comprehensive functional test cases covering various aspects of the HTML content, including navigation flows, form interactions, edge cases, dynamic content handling, user authentication and authorization, accessibility, and data manipulation operations.

- **User Roles and Permissions**:  The application considers different user roles, permissions, and access levels that may affect the UI's behavior during user interactions.

- **Edge Case Handling**: Potential edge cases, boundary conditions, and alternative scenarios are identified and incorporated into the test cases.

- **Structured Output**: The final output is a well-structured JSON format as shown, making it easy to integrate with other testing frameworks or tools.

```json
[
    {
        "userflow_name": "User Flow Name",
        "test_cases": [
            {
                "test_case_id": "TC_id",
                "test_case_description": "Test case description",
                "dependencies": "List of dependencies",
                "test_steps": "Steps to execute the test case",
                "expected_result": "Expected result of the test case"
            },
            
        ]
    },
    
]
```




## Getting Started

To get started with the HTML Test Case Generation Tool, follow these steps:

1. Clone the repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up the necessary environment variables (e.g., AzureOpenAI API key(or any other Model provider like Anthropic, Gemini etc.), deployment names, endpoints etc.)
4. Run the Flask application 
5. Send a POST request to the `/htmlagent` endpoint with the HTML content you want to analyze in the request body. Here is the JSON Schema for the request Payload :

 ```json
 {
    "html": "Your Stringified HTML content"
 }
 ```

## Contributing

As an open-source project, contributions are highly encouraged! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the project's coding conventions and guidelines.

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Create a new Pull Request on the original repository


