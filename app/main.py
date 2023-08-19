from fastapi import APIRouter, FastAPI, File, UploadFile, status

from app.config import get_settings
from app.models import Suggestion
from app.read_cv import read_cv
from app.suggester import Suggester

app = FastAPI()
router = APIRouter()

# Getting the application settings from configuration file
settings = get_settings()

class Controller:
    """
     Defining a controller class and loadingthe model before inferencing
    """
    def __init__(self) -> None:
        print('Loading the model...')
        self.model = Suggester(f'{settings.model_path}')
        print('Model has been loaded.')

    def categorize_article(self, CvIn) -> Suggestion:
        """
        getting prediction from model
        """
        resp = self.model.predict(f"{CvIn}")
        return resp

category_controller = Controller()

# Endpoint to upload Cvs and suggest them suitable job
@app.post("/upload",response_model=Suggestion, status_code=status.HTTP_201_CREATED)
def upload(file: UploadFile = File(...)):
    """
    upload file and returning the suggestion
    """
    try:
        contents = file.file.read()

         # Saving the file to a directory on the server
        with open(f"{settings.cv_dir}/{file.filename}", 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

     # Reading the text from the uploaded file
    doc = read_cv(f"{settings.cv_dir}/{file.filename}")

    return category_controller.categorize_article(doc)

# Starting the service and including the endpoint router
print("starting service with settings = {settings}")
app.include_router(router, prefix=settings.prefix)
