from textwrap import dedent
from crewai import Task
from typing import List ,Dict ,Union
from pydantic import BaseModel ,Field, root_validator


class TestCase(BaseModel):
    test_case_id: str = Field(description="The unique identifier for the test case")
    test_case_description: str = Field(description="The description of the test case")
    dependencies: str = Field(description="The dependencies of the test case")
    test_steps: str = Field(description="The steps to execute the test case")
    expected_result: str = Field(description="The expected result of the test case")

class TestFlow(BaseModel):
    userflow_name: str = Field(description="The name of the user flow")
    test_cases: List[TestCase] = Field(description="The list of test cases for the user flow")

class TestList(BaseModel):
    test_flows: List[TestFlow] = Field(description="The list of user flows with test cases")

# ```json
# [
#     {
#         "userflow_name": "User Flow Name",
#         "test_cases": [
#             {
#                 "test_case_id": "TC_id",
#                 "test_case_description": "Test case description",
#                 "dependencies": "List of dependencies",
#                 "test_steps": "Steps to execute the test case",
#                 "expected_result": "Expected result of the test case"
#             },
#             ... (more test cases)
#         ]
#     },
#     ... (more user flows)
# ]
# ```

#1st json structure
# ```json
# {{{{'userflow name'}}
#     {{'test_case_id'}}: {{TC_id}},
#     {{'test_case_description'}}: {{Test case description}},
#     {{'dependencies'}}: {{List of dependencies}},
#     {{'test_steps'}}: {{Steps to execute the test case}},
#     {{'expected_result'}}: {{Expected result of the test case}}
# }}
# ```

# class TestCase(BaseModel):
#     userflow_name: str = Field(description="The name of the user flow")
#     test_case_id: str = Field(description="The unique identifier for the test case")
#     test_case_description: str = Field(description="The description of the test case")
#     dependencies: str = Field(description="The dependencies of the test case")
#     test_steps: str = Field(description="The steps to execute the test case")
#     expected_result: str = Field(description="The expected result of the test case")

# class TestList(BaseModel):
#     testcase_module: List[TestCase]=Field(description="The list of test cases")

#changes for first json structure

# # class TestFlow(BaseModel):
# #     userflow_name: str
# #     test_cases: List[TestCase] = Field(description="The list of test cases")

# class TestList(BaseModel):
#     test_flows: List[TestFlow] = Field(description="The list of user flows")                                                                                            

# class TestList(BaseModel):
#     userflows: List[Dict[str, Union[str, List[TestCase]]]] = Field(description="The list of user flows")



class TestHTMLTasks():
    def summarizing_task(self, agent, snippet):
        return Task(
            description=dedent(f"""
You will analyze the provided HTML content and identify its key components, functionalities, and potential user interactions. This analysis will serve as the foundation for generating functional test cases. Follow these instructions:

Instructions:
- Review the HTML structure and identify elements such as links, buttons, forms, dropdowns, navigation menus, and any other interactive components.
- Understand the purpose and context of the web page or application based on the HTML content (e.g., e-commerce website, blog, dashboard, etc.).
- Identify the key functionalities and user interactions represented by the HTML elements (e.g., search functionality, product filtering, form submission, etc.).
- Outline the potential positive , negative and  edge cases or boundary conditions that could affect the application's behavior during user interactions.
- Create a concise summary that captures the identified key components, functionalities, user interactions, and potential edge cases.

HTML:
----
{snippet}

Expected Output:
- A well-structured summary of the HTML content, highlighting its key components, functionalities, user interactions, and potential edge cases.
- This summary will serve as the foundation for generating comprehensive functional test cases in the subsequent task.

"""),
            expected_output="YYour final output should be the summary that will serve as the foundation for generating comprehensive functional test cases.",
            agent=agent
        )

    def test_case_generation_task(self, agent, snippet, context):
        return Task(
            description=dedent(f"""
You will create comprehensive functional test cases based on the provided HTML content and the summary generated in the previous task. Follow these instructions:

Instructions:
- Review the provided HTML content and the summary from the previous task.
- Identify all possible user interactions and scenarios based on the functionalities and components outlined in the summary.
- Consider the dependencies and relationships between different elements and their expected behaviors during user interactions.
- Create functional test cases that cover a wide range of scenarios, including positive and negative test cases and edge cases.
- Do not include any testcases involving code or related to HTML code itself.
- Ensure that the test cases are realistic and accurately reflect potential user interactions and behaviors.
- Anything inside "{{{{ }}}}" is a placeholder; replace these values with appropriate values wherever you know the value.
- Generate functional test cases that cover the following aspects:
    - Navigation flow (e.g., clicking on links, navigating menus).
    - Form interactions (e.g., filling out fields, submitting forms).
    - Edge cases (e.g., invalid input, empty fields, broken links).
    - Handling of dynamic content (e.g., scripts, AJAX).
    -But do not include any test cases involving code or related to HTML code itself , only and only functional test cases.
- Ensure that the test cases are comprehensive, covering all possible scenarios including positive,negative test cases and edge cases identified in the summary.
- Structure the test cases in the following manner of list of dictionaries where each dictionary represents a test case:
```json
[
    {{
        "userflow_name": "User Flow Name",
        "test_cases": [
            {{
                "test_case_id": "TC_id",
                "test_case_description": "Test case description",
                "dependencies": "List of dependencies",
                "test_steps": "Steps to execute the test case",
                "expected_result": "Expected result of the test case"
            }},
            
        ]
    }},
    
]
```
HTML:
----
{snippet}

Expected Output:
-A comprehensive set of well-structured functional test cases covering all aspects of the HTML content, including navigation, forms, edge cases, accessibility, dynamic content, and styling.
-Test cases are comprehensive, covering all possible scenarios including positive, negative test cases and edge cases.
-The test cases should be organized and follow best practices for test case writing.
-The output should be a JSON string representation of the test cases.Your final answer should be a valid JSON object with the specified structure in Marked down format.
"""),
            expected_output="Your final answer should be a valid JSON object with the specified structure in Marked down format.",
            context=[context],
            agent=agent,
            #output_json=TestFlow
        )

    def test_case_verification_task(self, agent, snippet, context):
        return Task(
            description=dedent(f"""
You will verify the functional test cases generated by the software engineer and provide feedback for improvements. Follow these instructions:

Instructions:
- Review the provided HTML content and the summary from the previous tasks.
- Evaluate the functional test cases generated by the software engineer based on the following criteria:
    - Coverage of all HTML elements, functionalities, and potential user interactions
    - Handling of edge cases, boundary conditions, and alternative scenarios
    - Adherence to best practices for functional test case writing
    - Completeness and comprehensiveness of the test cases
    - Accuracy and consistency with the provided HTML content and summary
- Identify any missing functional test cases, inconsistencies, or areas for improvement.
- Provide detailed feedback and suggestions for enhancing the functional test cases, ensuring they are comprehensive and align with industry standards.

Evaluation Criteria:
- Completeness: Test cases cover all aspects of the HTML content, including navigation, forms, edge cases, accessibility, dynamic content, and styling.
- Accuracy: Test cases accurately reflect the provided HTML content, summary, and potential user interactions.
- Structure: Test cases are well-structured, organized, and follow best practices for test case writing.
- Clarity: Test cases are clear, concise, and easy to understand.
- Feasibility: Test cases are realistic and can be executed in practice.

HTML:
----
{snippet}

Expected Output:
- A detailed final list of functional test cases, including their descriptions and expected results.
- A detailed evaluation of the functional test cases provided by the software engineer, highlighting strengths, weaknesses, and areas for improvement.
- Specific feedback and suggestions to enhance the comprehensiveness, accuracy, and adherence to industry standards of the functional test cases.
- The output should only be a JSON string representation of the final list of functional test cases and the evaluation feedback nothing else.Like this:
```json
[
    {{
        "userflow_name": "User Flow Name",
        "test_cases": [
            {{
                "test_case_id": "TC_id",
                "test_case_description": "Test case description",
                "dependencies": "List of dependencies",
                "test_steps": "Steps to execute the test case",
                "expected_result": "Expected result of the test case"
            }},
            
        ]
    }},
    
]
```
"""),
            expected_output="Your final output should be a final list of functional test cases generated and its description and expected results, along with the detailed evaluation and feedback on the test cases provided by the software engineer. The output should be a JSON string representation of the final list of functional test cases and the evaluation feedback.",
            context=[context],
            agent=agent,
            #output_json=TestList
        )

                               