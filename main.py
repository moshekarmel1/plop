import os

from dotenv import load_dotenv

from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Setup environment variables for OpenAI & Pinecone
load_dotenv()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
PINECONE_ENV = os.environ['PINECONE_ENV']

# Setup a connection to the OpenAI Embeddings
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')

# Setup a connection to the Pinecone Vector Database to store the mappings
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)
index_name = 'wiki'
index = pinecone.Index(index_name)
search = Pinecone(index, embeddings.embed_query, 'text')
llm = OpenAI(temperature=0, model_name='text-davinci-003')
chain = load_qa_chain(llm, chain_type='stuff')

while True:
    query = input('Enter a query: ')
    docs = search.similarity_search(query, include_metadata=True)
    print(query)
    openai_response = llm(query)
    print('OpenAI says: ')
    print(openai_response)
    response = chain.run(input_documents=docs, question=query)
    print('Wiki says: ')
    print(response)
