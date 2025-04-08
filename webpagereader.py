from llama_index.readers.google import GoogleDocsReader
from llama_index import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv
load_dotenv()
def main(url: str)->None:
    # Step 1: Load the document from the provided URL (HTML to Text)
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is the history of generative ai")
    print (response)

    if __name__ == "__main__":
        main(url="https://medium.com/@social_65128/the-comprehensive-guide-to-understanding-generative-ai-c06bbf259786")