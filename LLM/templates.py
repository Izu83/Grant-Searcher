from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the Mistral model and tokenizer from Hugging Face
model_name = "mistralai/Mistral-7B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# Create a text generation pipeline
text_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7
)

# Wrap it with LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=text_pipeline)

# Interactive loop
while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("Exiting...")
        break
    response = llm.invoke(question)
    print("AI:", response)
