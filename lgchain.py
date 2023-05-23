
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.output_parsers import CommaSeparatedListOutputParser
from sqlalchemy import create_engine, Table, Column,select
import os
from dotenv import load_dotenv
from langchain.prompts import  PromptTemplate
from langchain.llms import AzureOpenAI
from snowflake.sqlalchemy import URL
from langchain.chains import SQLDatabaseSequentialChain
from langchain.prompts import PromptTemplate
import openai
import streamlit as st
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase

from langchain.agents import AgentExecutor



load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://aopai.openai.azure.com/"
openai.api_version = "2022-12-01"
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_TYPE"] = "azure"

user= os.environ['USER']
password=os.environ['PASS']
account=os.environ['ACCT']
database=os.environ['DBS']
schema=os.environ['schema']
role=os.environ['role']
warehouse=os.environ['warehouse']


_DEFAULT_TEMPLATE = """You're a senior SQL developer. You have to write sql code in snowflake database based on the following question. Also you have to ignore the sql keywords and give a one or two sentences about how did you arrive at that sql code. display the sql code in the code format (do not assume anything if the column is not available then say it is not available, do not make up code).
If you don't know the answer, just say "Hmm, I'm not sure. I am trained only to answer sql related queries. Please try again." Don't try to make up an answer
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: " Tables referred :
          The SQL Query generated :  
          Final answer : "

Question: {input}"""


PROMPT = PromptTemplate(
    input_variables=["input",], template=_DEFAULT_TEMPLATE)

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="'You\'re a senior SQL developer. You have to write sql code in snowflake database based on the following question. Also you have to ignore the sql keywords and give a one or two sentences about how did you arrive at that sql code. display the sql code in the code format (do not assume anything if the column is not available then say it is not available, do not make up code).\nIf you don\'t know the answer, just say Hmm, I\'m not sure. I am trained only to answer sql related queries. Please try again. Don\'t try to make up an answer\nUse the following format:\n\nQuestion: Question here \nSQLQuery: SQL Query to run \nSQLResult: Result of the SQLQuery\nAnswer: \nIf someone asks for the table foobar, they really mean the employee table.\n\nQuestion: {input}'.\n{format_instructions} ",
    input_variables=["input"],
    partial_variables={"format_instructions": format_instructions}
)

"""engine = create_engine(URL(
        account = account,
        user = user,
        password = password,
        database = database,
        schema = schema,
        warehouse = warehouse,
        role=role
))
"""

llm = AzureOpenAI(deployment_name="SnowSQL", model_name="text-davinci-003",temperature=0)

#db = SQLDatabase(engine)
conn_string = f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}"
db = SQLDatabase.from_uri(conn_string,sample_rows_in_table_info=1)
toolkit = SQLDatabaseToolkit(llm=llm, db=db)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

def chain(ip):
        #r_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True,prompt=PROMPT,)
        r_chain=agent_executor = create_sql_agent(
                llm=llm,
                 toolkit=toolkit,
                 verbose=True
                )
        #op = AgentExecutor.run(ip)
        op =r_chain.run(ip)
        return op

