from textwrap import dedent
from crewai import Task

class TestHTMLTasks():
    def summarizing_task(self, agent, snippet):
        return Task(
            description=dedent(f"""
You will analyze the provided HTML content and identify its key components, functionalities, and potential user interactions. This analysis will serve as the foundation for generating functional test cases. Follow these instructions:

Instructions:
- Review the HTML structure and identify elements such as links, buttons, forms, dropdowns, navigation menus, popups, tooltips, accordions, tabs,and any other UI components possible.
- Understand the purpose and context of the web page or application based on the HTML content (e.g., e-commerce website, blog, dashboard,  single-page application, etc.).
- Identify the key functionalities and user interactions represented by the HTML elements (e.g., search functionality, product filtering, form submission,navigation, data entry, user authentication, etc.).
- Consider different user roles, permissions, and access levels that may affect the application's behavior during user interactions.
- Outline the potential positive , negative and  edge cases or boundary conditions that could affect the application's behavior during user interactions(e.g., invalid input, empty fields, broken links, accessibility issues, responsiveness, etc.).
- Create a concise summary that captures the identified key components, functionalities, user interactions, and potential edge cases.

HTML:
----
{snippet}

Expected Output:
- A well-structured summary of the HTML content, highlighting its key components, functionalities, user interactions, and potential edge cases, user flows, and any other relevant information.
- This summary will serve as the foundation for generating comprehensive functional test cases in the subsequent task.

"""),
            expected_output="YYour final output should be the comprehensive summary that will serve as the foundation for generating comprehensive functional test cases.",
            agent=agent
        )

    def test_case_generation_task(self, agent, snippet, context):
        return Task(
            description=dedent(f"""
You will create comprehensive functional test cases based on the provided HTML content and the summary generated in the previous task. Follow these instructions:

Instructions:
- Review the provided HTML content and the comprehensive summary from the previous task.
- Identify all possible user interactions ,scenarios and user flows based based on the functionalities ,components and user roles outlined in the summary.
- Consider the dependencies and relationships between different elements and their expected behaviors during user interactions.
- Create functional test cases that cover a wide range of scenarios, including positive test cases ,negative test cases and edge cases , as well as different user roles, permissions, and access levels.
- Do not include any testcases involving code or related to HTML code itself.
- Ensure that the test cases are realistic and accurately reflect potential user interactions , behaviors and flows.
- Anything inside "{{{{ }}}}" is a placeholder; replace these values with appropriate values wherever you know the value.
- Generate functional test cases that cover the following aspects:
    - Navigation flow (e.g., clicking on links, navigating menus, breadcrumbs, pagination).
    - Form interactions (e.g., filling out fields, submitting forms, validations, error handling).
    - Edge cases (e.g., invalid input, empty fields, broken links, accessibility issues, responsiveness).
    - Handling of dynamic content (e.g., scripts, AJAX, real-time updates, websockets).
    - User authentication and authorization (e.g., login, logout, user roles, permissions).
    - Accessibility and usability (e.g., keyboard navigation, screen reader compatibility).
    - Data manipulation and CRUD operations (e.g., create, read, update, delete data).
    - But do not include any test cases involving code or related to HTML code itself , only and only functional test cases.
- Ensure that the test cases are comprehensive, covering all possible scenarios including positive,negative test cases and edge cases identified in the summary.
- Structure the test cases in the following manner of list of dictionaries where each dictionary represents a test case:
```json
    {{
        "test_cases": [
            {{
                "test_case_description": "Test case description",
                "dependencies": "List of dependencies",
                "test_steps": "Steps to execute the test case",
                "expected_result": "Expected result of the test case"
            }},
            
        ]
    }}, 
```
HTML:
----
{snippet}

Expected Output:
-A comprehensive set of well-structured functional test cases covering all aspects of the HTML content, including navigation, forms, edge cases, accessibility, dynamic content, and styling.
-Test cases are comprehensive, covering all possible scenarios including positive, negative test cases, and edge cases for different user roles, permissions, and access levels
-The test cases should be organized and follow best practices for test case writing.
-The output should be a JSON string representation of the test cases.Your final answer should be a valid JSON object with the specified structure in Marked down format.
"""),
            expected_output="Your final answer should be a valid JSON object with the specified structure in Marked down format.",
            context=[context],
            agent=agent,
            
        )


                               