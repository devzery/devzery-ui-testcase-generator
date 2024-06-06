import json
import os

from langchain_openai import AzureOpenAIEmbeddings
from crewai import Crew
from tasks import TestHTMLTasks
from agents import HTMLAgents
from dotenv import load_dotenv

load_dotenv()

tasks = TestHTMLTasks()
agents = HTMLAgents()

class TestCrew:
    def __init__(self,  HTMLSnippet):
            self.HTMLSnippet = HTMLSnippet
            print("HTML: ", HTMLSnippet)
        
    def kickoff_crew(self):
          #AGENTS
          summarizer_agent=agents.summarizer_agent()
          test_case_generator_agent=agents.test_case_generator_agent()
          #test_case_verifier=agents.test_case_verifier()

          #TASKS
          sumamrise_task=tasks.summarizing_task(summarizer_agent,self.HTMLSnippet)
          TC_generation_task=tasks.test_case_generation_task(test_case_generator_agent,self.HTMLSnippet,sumamrise_task)
          #TC_verification_task=tasks.test_case_verification_task(test_case_verifier,self.HTMLSnippet,TC_generation_task)

          crew=Crew(
                agents=[
                    summarizer_agent,
                    test_case_generator_agent,
                    #test_case_verifier
                ],
                tasks=[
                    sumamrise_task,
                    TC_generation_task,
                    #TC_verification_task
                ],
                verbose=True,
          )
          return crew
                
    


