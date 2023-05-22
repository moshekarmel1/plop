# plop
Python, Langchain, OpenAI, &amp; Pinecone stack

## What does it do?

Imagine if ChatGPT had context of your specific data and prioritized it while answering.
This project allows you to easily take some data that you have (like a Wiki, knowledge base, etc.), and allows you to query OpenAI with the context of your own data.

## What do I need to get setup

1. Get an `OPENAI_API_KEY` from your openai.com account. NOTE: You may need to pay $ for this. I tried the free version but it didn't work properly because I kept getting rate limited.
2. Setup a free Pinecone DB instance and grab the `PINECONE_API_KEY` and `PINECONE_ENV` variables.
3. Create a file called `.env` with the environment variables. It should be based on the `.env.example` file.
4. Install the Dependencies with `pip install -r requirements.txt`
5. Run `python loader.py` (one time) to load up some documents into the Pincone Vector DB, and use the Embeddings to save them in a way that can be easily queried later.

## How do I use it?

Run `python main.py` to query the Wiki system with your questions.

## What are the peices?

1. [Python](https://www.python.org/) is one of the most popular programming languages and is the de facto Language for AI/ML work.
2. [Langchain](https://python.langchain.com/en/latest/index.html) is a framework for developing applications powered by language models.
3. [OpenAI](https://openai.com/) is an AI research and deployment company. They have amazing tools and an API that allows easy access.
4. [Pinecone](https://www.pinecone.io/) is a cloud hosted Vector Database, which allows your AI to have long-term memory.

## Inspired by

[This video](https://www.youtube.com/watch?v=h0DHDp1FbmQ) and [This Document](https://python.langchain.com/en/latest/use_cases/question_answering.html)
