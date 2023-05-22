# plop
Python, Langchain, OpenAI, &amp; Pinecone stack

## What does it do?

Imagine if ChatGPT had context of your specific data and prioritized it while answering.
This project allows you to easily take some data that you have (like a Wiki, knowledge base, etc.), and allows you to query OpenAI with the context of your own data.

## How do I use it?

Create a file called `.env` with the environment variables. It should be based on the `.env.example` file.

Install the Dependencies with `pip install -r requirements.txt`

Run `python loader.py` (one time) to load up some documents into the Pincone Vector DB, and use the Embeddings to save them in a way that can be easily queried later.

Run `python main.py` to query the Wiki system with your questions.

## Inspired by

[This video](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
