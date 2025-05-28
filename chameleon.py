from collections.abc import Callable

import openai
from openai import OpenAI


class Chameleon:
    openai: OpenAI

    def __init__(self, openai_builder: Callable[[], OpenAI] = lambda: OpenAI()):
        self.openai = openai_builder()
        self.scope = {}

    def __getattr__(self, method_name: str):
        def execute(*args, **kwargs):
            retries = 0

            while retries < 5:
                if retries > 0 or not method_name in self.scope:
                    self.__generate_method(method_name, *args, **kwargs)

                try:
                    return self.scope[method_name](*args, **kwargs)
                except Exception as e:
                    print(f"Error executing {method_name}: {e}")
                    retries += 1

            raise Exception(f"Failed to execute {method_name} with arguments {args} and keyword arguments {kwargs}")

        return execute

    def __generate_method(self, method_name: str, *args, **kwargs):
        retries = 0

        while retries < 5:
            response = openai.responses.create(
                input=f"""
                    Generate the a python function called {method_name} that creates the appropriate output for arguments {args}
                    and keyword arguments {kwargs}.
    
                    The response should only contain the function definition, and must be valid python.
                    It must take arguments {args} and keyword arguments {kwargs}.

                    The only non-stdlib libraries you are allowed to use are
                    - requests
                    - openai
    
                    Do not include any other text in the response, even backticks.
                    """,
                model="gpt-4.1",
            )

            function_definition = response.output[0].content[0].text
            try:
                exec(function_definition, globals(), self.scope)
                return
            except SyntaxError as e:
                print(f"Syntax error generating {method_name}: {e}")
                retries += 1

        raise Exception(f"Failed to generate method with correct syntax for {method_name} with arguments {args} and keyword arguments {kwargs}")
