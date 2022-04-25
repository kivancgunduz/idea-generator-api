import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#response = openai.Completion.create(engine="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)




class Generator():
    """
    A Class that generate idea for user based GPT-3 API.
    """
    def __init__(self, question:str, number_of_idea: int, workshop_method:str, enhaced:bool = False) -> None:
        """
        A constructor function for Generator class.
        :param question: A question that user want to ask.
        :param number_of_idea: Number of idea that user want to get.
        :param enhaced: A boolean value that indicate if user want to get enhaced idea or not.
        :param workshop_method: A string value that indicate which workshop method user want to use.
        """
        self.question:str = question
        self.number_of_idea:int = number_of_idea
        self.enhaced:bool = enhaced
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
        
    def openai_completion(prompt : str, engine : str, max_tokens : int, temperature : float, top_p : float, stop=None, presence_penalty : float, frequency_penalty : float) -> str:
        """
        Asks openai for completion
        and returns the text string of the first choice
        """
    response = openai.Completion.create(
        prompt=prompt,
        engine=engine,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty
       
)
    print(response)
    return response.choices[0].text

    # def generate_idea(self) -> bool:
    #     """
    #     A Funtion that generate idea for user based GPT-3 API.
    #     :return: None
    #     """
    #     if self.connect_openai():
    #         """
    #         If api connection is created, then generate idea.
    #         """
    #         if self.enhaced:
    #             """
    #             If user want to get enhaced idea, then generate idea with enhaced parameter.
    #             """
    #             # @TODO: Add a try catch block for this function. @gio
    #         else:
    #             """
    #             If user want to get normal idea, then generate idea with normal parameter.
    #             """

    #             # @TODO: Add a try catch block for this function. @gio
    #     else:
    #         pass


        