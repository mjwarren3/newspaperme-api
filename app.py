from fastapi import FastAPI
from langserve import add_routes

from category import category_chain

from events_summarizer import summary_chain


# 2. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)


# 3. Adding chain route
add_routes(
    app,
    category_chain,
    path="/category_chain",
)

# 3. Adding chain route
add_routes(
    app,
    summary_chain,
    path="/summary_chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)