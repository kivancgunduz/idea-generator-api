import os
import openai
# ? from utils import preprocessing 
import requests


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
        ? :param crazy: A boolean value that indicate if user want to get an unusual suggestions or a more normal one.
        :param workshop_method: A string value that indicate which workshop method user want to use.
        """
        #self.question:str = question
        self.output_data:str = question #?? from pre-processing or direct from user interface
        self.number_of_idea:int = number_of_idea
        self.enhaced:bool = enhaced
        # self.crazy:bool = crazy
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
            if self.enhaced:
                """
                If user want to get enhaced idea, then generate idea with enhaced parameter.
                """
                # @TODO: Add a try catch block for this function. @gio
            else:
                """
                If user want to get normal idea, then generate idea with normal parameter.
                """

                # @TODO: Add a try catch block for this function. @gio

            # if self.crazy:
            #     """
            #     If user want to get user want to get an unusual suggestions, then generate idea with crazy parameter.
            #     """
            #     # @TODO: Add a try catch block for this function. @gio
            # else:
            #     """
            #     If user want to get normal idea, then generate idea with normal parameter.
            #     """

            #     # @TODO: Add a try catch block for this function. @gio
        else:
            pass

            if self.workshop_method is "How might we ... ?":
                """
                use process_hmw() to generate ideas
                """
                return # self.idea_list:list = [] ?
            elif self.workshop_method is "Opposite thinking":
                """
                use process_opposite () to generate ideas
                """
                return
            elif self.workshop_method is "What is the worst possible idea about ...?":
                """
                use process_bad_idea () to generate ideas
                """
                return
            elif self.workshop_method is "Ask any question!":
                """
                use process_free_text() to generate ideas
                """
                return
            else:
                # default to "Ask any question!"
                return

            return

            # @TODO: Add a try catch block for this function. 

 # r = requests.post("https://api.openai.com/v1/engines/{engine_id}/completions", data = payload)

# payload = 
#  {
#   "question": "Say this is a test",
#   "max_tokens": 5,
#   "temperature": 1,
#   "top_p": 1,
#   "n": 1,
#   "stop": "\n"
#    }




    # def _completion(question, engine="ada", max_tokens=64, temperature=0.7, top_p=1, stop=None, presence_penalty=0, frequency_penalty=0, n=1):
    # logger.debug("""CONFIG:
    # Question: {0}
    # Temperature: {1}
    # Engine: {2}
    # Max Tokens: {3}
    # Top-P: {4}
    # Stop: {5}
    # Presence Penalty {6}
    # Frequency Penalty: {7}
    # N: {8}"""
    #              .format(repr(question), temperature, engine, max_tokens, top_p, stop, presence_penalty, frequency_penalty, n))



    # response = openai.Completion.create(engine=engine,
    #                                     question=question,
    #                                     max_tokens=max_tokens,
    #                                     temperature=temperature,
    #                                     top_p=top_p,
    #                                     presence_penalty=presence_penalty,
    #                                     frequency_penalty=frequency_penalty,
    #                                     stop=stop,
    #                                     n=n, #self.number_of_idea:int = number_of_idea
    #                                     )
    # logger.debug("GPT-3 Completion Result: {0}".format(response))
    # return response

