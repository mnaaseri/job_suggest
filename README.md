# Job Position Suggestion using a NLI Classifier


In this project the users uploads their CV, and the classifier suggests her a job based on the text of the CV. The suggestion will be made between candidates that we provided. 

## API

- **Endpoint**: `/upload`
- **Method**: `POST`
- **Request**: The request should contain the CV file to be uploaded.

- **Response**
```
{
    "Job": "str"
    "confidence": "float"
}
```

## RUN Docker 

docker compose up


## Dependencies

The application requires the following Python packages:

- PyPDF2
- python-docx
- fastapi
- uvicorn
- pydantic
- transformers
- tensorflow

These can be installed using pip:

```bash
pip install -r requirements.txt

To start the application without docker run the following command: 

uvicorn app.main:app --reload
