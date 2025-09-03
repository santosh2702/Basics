from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Translate the following text to French:\n{text}"
)
print(template.format(text="Good morning"))
