from typing import Tuple

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chains import LLMChain, SequentialChain

def build_query_chain(llm: OpenAI) -> Tuple[SequentialChain ,str, StructuredOutputParser]:

    response_schemas = [
        ResponseSchema(name="positive_article", description="긍정 담론에 대한 뉴스레터"),
        ResponseSchema(name="negative_article", description="부정 담론에 대한 뉴스레터")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    response_format= output_parser.get_format_instructions()


    prompt = PromptTemplate.from_template(
        template="""
            너는 이슈와 이슈를 잘 나타내는 대표 키워드를 기반으로 이슈에 대한 반론을 친근한 반말 뉴스레터로 만드는 작가야
            이슈 : {issue_name} 
            긍정입장 대표 키워드: {positive_keyword}
            부정입장 대표 키워드: {negative_keyword}
            {response_format}
        """
    )

    query_chain = LLMChain(llm=llm, prompt=prompt, output_key='query')

    chain = SequentialChain(
        chains=[query_chain],
        input_variables=['issue_name', 'positive_keyword', 'negative_keyword'] + [ 'response_format'],
        output_variables=['query'],
        verbose=False
    )
    
    return chain, response_format, output_parser

