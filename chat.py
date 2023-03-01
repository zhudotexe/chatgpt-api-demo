import datetime

import openai
import tiktoken


class Chatterbox:
    def __init__(self, system_prompt: str, desired_response_tokens: int = 256, max_context_size: int = 4096):
        self.tokenizer = None
        self.system_prompt = system_prompt.strip()
        self.desired_response_tokens = desired_response_tokens
        self.max_context_size = max_context_size
        self.chat_history = []

    def load_tokenizer(self):
        """
        Load the tokenizer (from the internet if first run). See
        https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
        """
        self.tokenizer = tiktoken.get_encoding("gpt2")

    def get_truncated_chat_history(self):
        """
        Returns a list of messages such that the total token count in the messages is less than
        (4096 - desired_response_tokens).
        Always includes the system prompt and user's last prompt.
        """
        reversed_history = []
        system_prompt_len = len(self.tokenizer.encode(self.system_prompt))
        remaining = self.max_context_size - system_prompt_len - self.desired_response_tokens
        for message in reversed(self.chat_history):
            message_len = len(self.tokenizer.encode(message["content"]))
            remaining -= message_len
            if remaining > 0:
                reversed_history.append(message)
            else:
                break
        reversed_history.append({"role": "system", "content": self.system_prompt})
        return reversed_history[::-1]

    def chat_round(self):
        # get the user's chat input
        user_chat = input("==== You ====\n")
        self.chat_history.append({"role": "user", "content": user_chat.strip()})
        print()

        # get the model's output, save it to chat history
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.get_truncated_chat_history())
        message = completion["choices"][0]["message"]
        self.chat_history.append(message)
        response = message["content"]

        # and print the response
        print(f"==== ChatGPT ====\n{response}\n")

    def run(self):
        self.load_tokenizer()
        while True:
            self.chat_round()


if __name__ == "__main__":
    current_date = datetime.date.today()
    chatter = Chatterbox(
        "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. "
        f"Knowledge cutoff: 2021-09. Current date: {current_date}."
    )
    chatter.run()
