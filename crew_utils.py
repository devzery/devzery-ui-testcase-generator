from crewai import Crew ,Process
from tasks import TestHTMLTasks
from agents import HTMLAgents
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os



load_dotenv()

tasks = TestHTMLTasks()


class TestCrew:
    """
    A class representing a test crew.

    Args:
        HTMLSnippet (str): The HTML snippet to be used by the crew.

    Attributes:
        HTMLSnippet (str): The HTML snippet used by the crew.

    Methods:
        kickoff_crew: Starts the crew and returns the crew object.

    """
 
    def __init__(self, HTMLSnippet,llm=ChatOpenAI(model="gpt-4-0125-preview",openai_api_key=os.getenv("OPENAI_API_KEY","None"))):  #add in docs
        """
        Initializes a new instance of the TestCrew class.

        Args:
            HTMLSnippet (str): The HTML snippet to be used by the crew.

        """
        self.HTMLSnippet = HTMLSnippet
        self.llm=llm

    def kickoff_crew(self):
        """
        Starts the crew and returns the crew object.

        Returns:
            Crew: The crew object.

        """
        agents = HTMLAgents(llm=self.llm)
        summarizer_agent = agents.summarizer_agent()
        test_case_generator_agent = agents.test_case_generator_agent()
        

        
        sumamrise_task = tasks.summarizing_task(summarizer_agent, self.HTMLSnippet)
        testcase_generation_task = tasks.test_case_generation_task(test_case_generator_agent, self.HTMLSnippet, sumamrise_task)
        

        crew = Crew(
            agents=[
                summarizer_agent,
                test_case_generator_agent,
                
            ],
            tasks=[
                sumamrise_task,
                testcase_generation_task,
                
            ],
           process=Process.sequential
,
        )
        return crew
                
    


