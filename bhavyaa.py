import wikipediaapi
import openai

openai.api_key = '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'

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='bhavyaa-fetcher/1.0'
)

def display_sections(page_title):
    page = wiki_wiki.page(page_title)
    if not page.exists():
        print("Page doesn't exist.")
        return

    print(f"Sections available in '{page_title}':")
    for index, section in enumerate(page.sections):
        print(f"{index + 1}. {section.title}")

def fetch_section_text(page_title, section_number):
    page = wiki_wiki.page(page_title)
    if not page.exists():
        return "Page doesn't exist."

    sections = list(page.sections)
    if section_number < 1 or section_number > len(sections):
        return "Invalid section number."

    selected_section = sections[section_number - 1]
    return selected_section.text

def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def paraphrase_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Paraphrase the following text: {text}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Ask user for the Wikipedia page title
    page_title = input("Enter the Wikipedia page title: ")

    display_sections(page_title)

    section_number = int(input("Enter the section number to fetch text: "))

    selected_text = fetch_section_text(page_title, section_number)
    print("\nSelected Section Text:")
    print(selected_text)

    summarized_text = summarize_text(selected_text)
    print("\nSummarized Text:")
    print(summarized_text)

    paraphrased_text = paraphrase_text(summarized_text)
    print("\nParaphrased Text:")
    print(paraphrased_text)
