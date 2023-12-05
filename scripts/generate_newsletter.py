from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from dotenv import load_dotenv
from dynamodb.issue_keywords import IssueKeywords
from langchain.llms import OpenAI

from chain import build_query_chain


if __name__ == "__main__":
    ik = IssueKeywords()

    response = ik.query_by_issue_date("20231205")
    issue_keyword_data = response[0]

    llm = OpenAI(
        temperature=0.5,              
        max_tokens=2000,             
        model_name='gpt-4',  
    )
    chain, response_format, output_parser = build_query_chain(llm)
    response = chain.run(
        {
            'issue_name':issue_keyword_data["issue_name"],
            'positive_keyword':issue_keyword_data["positive_keyword"],
            'negative_keyword':issue_keyword_data["negative_keyword"],
            "response_format": response_format
        }
    )
    query = output_parser.parse(response)["positive_article"]
    print(query)