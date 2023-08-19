import json

from transformers import pipeline

from app.clean_text import clean_text
from app.config import get_settings

settings = get_settings()

with open(f'{settings.json_dir}/JOBS.json') as data:
    CATEGORIES = json.load(data)
    
candidate_labels = []
for value in CATEGORIES.values():
    candidate_labels.append(value)

print(candidate_labels)

class Suggester:
    """
    Use zero-shot model to suggest a job based on CV
    """
    def __init__(self, model_path:str):
        self.classifier = pipeline("zero-shot-classification", 
                            model=model_path, from_pt=True)   
    def predict(self, input_text: str):
        result = self.classifier(clean_text(input_text), candidate_labels, multi_label=True)

        job_suggestion = result['labels'][0]
        confidence = result['scores'][0]
        print(job_suggestion)

        return {
            "job_suggestion": job_suggestion,
            "confidence": confidence,
        }
            