import dotenv
dotenv.load_dotenv()


from chatbot_api.src.chains.hospital_cypher_chain import (
hospital_cypher_chain
)

question = """Which state had the lowest percent increase
           in Medicaid visits from 2022 to 2023?"""
response = hospital_cypher_chain.invoke(question)




print(response.get("result"))