# Example 1
# import fitz
#
# def extract_text_from_pdf(pdf_file_path):
#     try:
#         doc = fitz.open(pdf_file_path)
#         pdf_text = ""
#         for page_num in range(doc.page_count):
#             page = doc.load_page(page_num)
#             pdf_text += page.get_text("text")
#         doc.close()
#         return pdf_text
#     except Exception as e:
#         return f"Error extracting text: {e}"
#
# pdf_path = "E:/Mandar/Git/OpenAIChatbot/Landon-Hotel.pdf"
# extracted_text = extract_text_from_pdf(pdf_path)
#
# file = open("pdf_text", "w", encoding='utf-8')
# file.write(extracted_text)

# Example 2
# import requests
# from bs4 import BeautifulSoup
#
# target_url = "https://www.landonhotel.com"
#
# response = requests.get(target_url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     text = ""
#
#     for paragraph in soup.find_all('p'):
#         text += paragraph.get_text()
#
#     with open('website_text.txt', 'w') as text_file:
#         text_file.write(text)
#
#     print("Text extracted and saved successfully!")
#
# else:
#     print(f"Error: Failed to retrieve website content. Status code: {response.status_code}")

# Example 3
# from openai import OpenAI
# client = OpenAI()
#
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {
#       "role": "system",
#       "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
#     },
#     {
#       "role": "user",
#       "content": "The earliest successful AI program was written in 1951 by Christopher Strachey, later director of the Programming Research Group at the University of Oxford. Strachey’s checkers (draughts) program ran on the Ferranti Mark I computer at the University of Manchester, England. By the summer of 1952 this program could play a complete game of checkers at a reasonable speed. Information about the earliest successful demonstration of machine learning was published in 1952. Shopper, written by Anthony Oettinger at the University of Cambridge, ran on the EDSAC computer. Shopper’s simulated world was a mall of eight shops. When instructed to purchase an item, Shopper would search for it, visiting shops at random until the item was found. While searching, Shopper would memorize a few of the items stocked in each shop visited (just as a human shopper might). The next time Shopper was sent out for the same item, or for some other item that it had already located, it would go to the right shop straight away. This simple form of learning, as is pointed out in the introductory section What is intelligence?, is called rote learning. The first AI program to run in the United States also was a checkers program, written in 1952 by Arthur Samuel for the prototype of the IBM 701. Samuel took over the essentials of Strachey’s checkers program and over a period of years considerably extended it. In 1955 he added features that enabled the program to learn from experience. Samuel included mechanisms for both rote learning and generalization, enhancements that eventually led to his program’s winning one game against a former Connecticut checkers champion in 1962."
#     }
#   ],
#   temperature=0.5
# )
#
# print(response.choices[0].message.content)

# Example 4

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

prompt = open('website_text.txt', 'r').read()

hotel_assistant_template = prompt + """
You are the hotel manager of Landon Hotel, named "Mr. Landon". 
Your expertise is exclusively in providing information and advice about anything related to Landon Hotel. 
This includes any general Landon Hotel related queries. 
You do not provide information outside of this scope. 
If a question is not about Landon Hotel, respond with, "I can't assist you with that, sorry!" 
Question: {question} 
Answer: 
"""

hotel_assistant_prompt_template = PromptTemplate(
    input_variables=["question"],
    template=hotel_assistant_template
    )

llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0,
             api_key="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")

llm_chain = hotel_assistant_prompt_template | llm

def query_llm(question):
    print(llm_chain.invoke({'question': question}))

while True:
    query_llm(input())

