import torch
from transformers import AutoModel, AutoTokenizer, pipeline

class Model:
    
    def __init__(self, model_path: str):
        self.__model_path = model_path
        self.compute_device = 0 if torch.cuda.is_available() else -1
        self.summarizer = pipeline(
            "summarization",
            model_path,
            device= self.compute_device,
        )

    def model_serve(self,text_to_summarize: str):
        output = self.summarizer(
            text_to_summarize,
            min_length=16,
            max_length=256,
            no_repeat_ngram_size=3,
            encoder_no_repeat_ngram_size=3,
            repetition_penalty=3.5,
            num_beams=4,
            early_stopping=False,
        )
        return output
    