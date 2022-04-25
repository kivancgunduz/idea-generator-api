import os
import openai
from utils import preprocessing 
import requests


class Generator():
    """
    A Class that generate idea for user based GPT-3 API.
    """
    def __init__(self, prepared_question:str, number_of_idea: int, workshop_method:str, crazy:bool = False) -> None:
        """
        A constructor function for Generator class.
        :param prepared_question: A question that user want to ask.
        :param number_of_idea: Number of idea that user want to get.
        :param crazy: A boolean value that indicate if user want to get an unusual suggestions or a more normal one.
        :param workshop_method: A string value that indicate which workshop method user want to use.
        """
        self.prepared_question:str = prepared_question
        self.number_of_idea:int = number_of_idea
        self.crazy:bool = crazy
        self.workshop_method:str = workshop_method
        self.idea_list:list = []
        self.idea_list_enhaced:list = []
        self.api_key:str = os.getenv('OPENAI_API_KEY')

    def connect_openai(self) -> bool:
        """
        A function that create api connection.
        :return: A boolean value that indicate if api connection is created or not.
        """
        try:
            openai.api_key = self.api_key
        except openai.exceptions.InvalidAPIKeyError:
            return False
        else:
            return True
        
    def generate_idea(self) -> bool:
        """
        A Funtion that generate idea for user based on GPT-3 API.
        :return: None
        """
        if self.connect_openai():
            """
            If api connection is created, then generate idea.
            """
        if self.crazy:
            """
            If user want to get enhaced idea, then generate idea with enhaced parameter.
            """
        else:
            """
            If user want to get normal idea, then generate idea with normal parameter.
            """ 
            pass

    payload =  {
            "prompt": self.prepared_question,
            "max_tokens": 5,
            "temperature": 1,
            "top_p": 1,
            "n": self.number_of_idea,
            "stop": "\n"
            }

r = requests.post("https://api.openai.com/v1/engines/{engine_id}/completions", data = payload)


