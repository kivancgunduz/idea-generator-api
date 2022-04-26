
import os
import openai
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
        self.raw_result:dict = None
        self.idea_list:list = []
        self.idea_list_enhaced:list = []
        self.api_key:str = None
        self.payload:dict = {}

    def connect_openai(self) -> bool:
        """
        A function that create api connection.
        :return: A boolean value that indicate if api connection is created or not.
        """
        try:
            credential = open("data/api_credentials.json", "r")
            self.api_key = eval(credential.read())['openAI_api_key']
            print(self.api_key)
            openai.api_key = self.api_key
        except openai.exceptions.InvalidAPIKeyError:
            return False
        except FileNotFoundError:
            return False
        except openai.exceptions.InvalidRequestError:
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
            read_file = open("data/params_dict.txt", "r")
            params_dict = eval(read_file.read())
            if self.workshop_method == "hmw": self.payload = params_dict['payload']["hmw"]
            elif self.workshop_method == "opposite": self.payload = params_dict['payload']["opposite"]
            elif self.workshop_method == "bad idea": self.payload = params_dict['payload']["bad"]
            elif self.workshop_method == "free text": self.payload = params_dict['payload']["free"]
            
            #print(self.payload)
            self.raw_result = openai.Completion.create(**self.payload)
            #print(self.raw_result)
            #print(self.raw_result['choices'][0]['text'])
        else:
            """
            If api connection is not created, then return false.
            """
            return False
            

            
#gen = Generator("measure developer performance", 10, "hmw", False)
#gen.generate_idea()
