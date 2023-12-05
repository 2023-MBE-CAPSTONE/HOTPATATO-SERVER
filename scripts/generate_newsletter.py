import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from langchain.llms import OpenAI

from dynamodb.issue_keywords import IssueKeywords
from dynamodb.generated_articles import GeneratedArticles
from models.generated_article import GeneratedArticle
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
    query = output_parser.parse(response)

    ga = GeneratedArticles()
    data = {
        "issue_date": issue_keyword_data["issue_date"],
        "issue_name": issue_keyword_data["issue_name"],
        "positive_article": query["positive_article"],
        "negative_article": query["negative_article"],
    }
    data = GeneratedArticle(**data)
    response = ga.add_generated_article(data)
    print(response)