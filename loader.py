import time
import datetime
import os

from dotenv import load_dotenv

from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

start = time.perf_counter()

# Setup environment variables for OpenAI & Pinecone
load_dotenv()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
PINECONE_ENV = os.environ['PINECONE_ENV']

# Load in a local wiki of markdown files
loader = DirectoryLoader('../docs/', glob='**/*.md', loader_cls=UnstructuredMarkdownLoader)

data = loader.load()

print(f'You have {len(data)} documents(s) in your data')

# Setup a connection to the OpenAI Embeddings
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')

# Setup a connection to the Pinecone Vector Database to store the mappings
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)
index_name = 'wiki'

# Update the Pinecode index (in the Cloud) 
docsearch = Pinecone.from_texts([d.page_content for d in data], embeddings, index_name=index_name)

end = time.perf_counter()

duration = end - start

print(str(datetime.timedelta(seconds=duration)))
