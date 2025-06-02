from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

MODELS = {}

def load_models():
    global MODELS
    MODELS['code'] = pipeline("text-generation", 
        model="codellama/CodeLlama-7b-Instruct", 
        tokenizer="codellama/CodeLlama-7b-Instruct",
        device=0 if torch.cuda.is_available() else -1,
        max_new_tokens=512
    )
    MODELS['chat'] = pipeline("text-generation", 
        model="meta-llama/Meta-Llama-3-8B-Instruct", 
        tokenizer="meta-llama/Meta-Llama-3-8B-Instruct",
        device=0 if torch.cuda.is_available() else -1,
        max_new_tokens=512
    )

def get_model(task_type):
    return MODELS.get(task_type)
