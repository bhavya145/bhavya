import wikipediaapi
import openai

openai.api_key = 'OPEN_AI_API_KEY'

def display_sections(page_name):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(page_name)
    
    print("Sections available:")
    for index, section in enumerate(page.sections):
        print(f"{index + 1}. {section.title}")
    
    return page

def fetch_section_text(page, selected_section_index):
    selected_section = list(page.sections.values())[selected_section_index - 1]
    return selected_section.text if selected_section.exists() else None

def summarize_text_with_gpt3(text):
    prompt_text = f"This is a summarization task:\n{text}\n\nSummary:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_text}
        ],
        temperature=0.5,
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]

def paraphrase_text_with_gpt3(text):
    prompt_text = f"This is a paraphrasing task:\n{text}\n\nParaphrase:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_text}
        ],
        temperature=0.7,
        max_tokens=100
    )
    return response["choices"][0]["message"]["content"]


def main():
    page_name = input("Enter the Wikipedia page name: ")
    
    page = display_sections(page_name)
    
    selected_section_index = int(input("Enter the number of the section you want to summarize: "))
    
    selected_section_text = fetch_section_text(page, selected_section_index)
    
    summarized_text = summarize_text_with_gpt3(selected_section_text)
    print("Summarized text:")
    print(summarized_text)
    
    paraphrased_text = paraphrase_text_with_gpt3(summarized_text)
    print("\nParaphrased text:")
    print(paraphrased_text)
    
def display_sections(page_name):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0'
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent)
    page = wiki_wiki.page(page_name)
    
    print("Sections available:")
    for index, section in enumerate(page.sections):
        print(f"{index + 1}. {section.title}")
    
    return page

def fetch_section_text(page, selected_section_index):
    if selected_section_index > 0 and selected_section_index <= len(page.sections):
        selected_section = page.sections[selected_section_index - 1]
        if selected_section:
            return selected_section.text
    return None

if __name__ == "__main__":
    main()
