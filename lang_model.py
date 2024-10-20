from forms import UserCreateQA
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# tokenizer = AutoTokenizer.from_pretrained("fattahalilmi/output1")
# model = AutoModelForQuestionAnswering.from_pretrained("fattahalilmi/output1")

qa_pipeline = pipeline(
    "question-answering",
    model="fattahalilmi/question-answering",
    tokenizer="fattahalilmi/question-answering"
)

def predict(context, question):
    return qa_pipeline({
        'context': context,
        'question': question
    })