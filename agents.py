import os
from textwrap import dedent 
from crewai import Agent
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    openai_api_version=os.getenv("openai_api_version"),
    azure_deployment=os.getenv("DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_type="azure",
)

embeddings_model = AzureOpenAIEmbeddings(
    openai_api_version="2023-08-01-preview",
    deployment=os.getenv("embeddings_deployment_name"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
) 

class HTMLAgents():
    def summarizer_agent(self):
        return Agent(
            llm=llm,
            role='Expert in summarizing HTML content',
            goal='Summarize the HTML content to a brief summary',
            backstory=dedent("""\
                             An expert in  summarizing HTML content and capturing all the nuances"""),
            allow_delegation=False,
            verbose=True,


        )
            
           
    def test_case_generator_agent(self):
        return Agent(
            llm=llm,
            role='HTML Tester and Frontend Lead Engineer',
            goal='Create robust test cases for HTML by analysing the HTML content provided along with the summary',
            backstory=dedent("""\
                            You are a software engineer specializing in testing HTML content for web applications.
                         With an exceptional eye for detail and a talent for uncovering hidden issues, you meticulously generate HTML test cases.
                         Your role involves ensuring that all HTML elements and structures function correctly and are accessible, providing both positive and negative test scenarios to cover a wide range of potential user interactions and edge cases.
                         You have a deep understanding of HTML elements, their usage, and potential issues or edge cases that might arise during testing. You are familiar with common HTML elements such as headers, navigation menus, forms, links, scripts, and styles, and you understand how they interact with each other and impact the overall functionality of a web page.
                         You also have experience in handling different types of test cases, including positive test cases (verifying expected behavior), negative test cases (verifying error handling and edge cases), and accessibility test cases (ensuring web content is accessible to users with disabilities). 
                             """),
            allow_delegation=False,
            verbose=True,
        )
        


    def test_case_verifier(self):
        return Agent(
            llm=llm,
            role='Chief Software Quality Control Engineer',
            goal='Ensure that the test cases generated are correct and verify with respect to HTML provided',
            backstory=dedent("""\
                            You feel that HTML test-case generators only do half of their jobs so you're super 
                            dedicated to reverify and make high quality testcases for HTML content""" 
                            ),
            allow_delegation=False,
            verbose=True,
        )
            
                   
