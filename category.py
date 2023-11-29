from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import OPENAI_API_KEY

chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a category, and you should generate {num_of_objects} objects in that category in a comma separated list.
ONLY return a comma separated list, and nothing more."""

human_template = "{category}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

category_chain = chat_prompt | chat_model
