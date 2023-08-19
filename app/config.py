from pydantic import BaseSettings

class Settings(BaseSettings):
    """Global configurations."""
    prefix: str = "/ai/job-suggestor-v1"
    json_dir: str = "./files"
    model_path: str = "cross-encoder/nli-deberta-base"
    cv_dir: str = "./cvs"

def get_settings():
    return Settings()
