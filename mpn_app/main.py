import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, service_clients, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Initialize the external service client
# external_service_client = ExternalServiceClient(base_url="http://external-service")

# # Initialize the orchestration service
# orchestration_service = OrchestrationService(external_service_client)

# @app.post("/submit-pib")
# async def submit_pib(document: PIBDocument):
#     try:
#         document_dict = document.dict()
#         response = orchestration_service.process_document(document_dict)
#         return JSONResponse(content={"message": "Document processed successfully", "response": response})
#     except ValidationError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/make-billing")
def create_billing(billing: schemas.BillingCreate, db: Session = Depends(get_db)):
# db_user = crud.get_submision(db, email=subsmission.email)
# if db_user:
#     raise HTTPException(status_code=400, detail="Email already registered")
    return service_clients.create_billing(db=db, billing=billing)