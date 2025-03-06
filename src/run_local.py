from langchain import hub
from typing_extensions import TypedDict
from typing_extensions import Annotated
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
load_dotenv()


# GROQ_API_KEY = os.getenv('GROQ_API_KEY')

os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

db = SQLDatabase.from_uri("sqlite:///mlflow.db")


llm = init_chat_model("llama3-8b-8192", model_provider="groq")
query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")



def write_query(ques_dict:dict):
    """Generate SQL query to fetch information."""
    prompt = query_prompt_template.invoke(
        {
            "dialect": db.dialect,
            "top_k": 10,
            "table_info": db.get_table_info(),
            "input": ques_dict["question"],
        }
    )
    
    result = llm.invoke(prompt)
    return {"query": result.content}



def execute_query(query_dic:dict):
    """Execute SQL query."""
    execute_query_tool = QuerySQLDataBaseTool(db=db)
    return {"result": execute_query_tool.invoke(query_dic["query"])}

# res=execute_query({"query":"SELECT COUNT(*) FROM runs;"})
# print(res)




