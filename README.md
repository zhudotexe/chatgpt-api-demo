# ChatGPT API Demo

This repository demonstrates how to use the newly-released (as of March 1, 2023) ChatGPT API.

**TL;DR**: Run `python chat.py` to have a chat with ChatGPT right from your terminal!

It demonstrates these concepts:

- Passing instructions via the system prompt
- Building up the message history through a continued conversation
- Truncating long conversations to fit within the model context

## Requirements

### Python

- Python 3.10+

To install Python dependencies, I recommend using a virtual environment. You can set one up by running:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

then, use the following command to install this project's dependencies:

```bash
$ pip install -r requirements.txt
```

### OpenAI API

You will also need to set your OpenAI API key, which you can find [here](https://platform.openai.com/account/api-keys).

To pass this API key to the project, set the `OPENAI_API_KEY` environment variable by running:

```bash
$ export OPENAI_API_KEY="<your API key here>"
```

(You could also add this to your shell profile so you don't have to do this every time.)

## Talking to ChatGPT

To chat with ChatGPT, simply run the following:

```bash
$ python chat.py
```

More options and arguments will be added to this demo in the future.
