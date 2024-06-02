from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from schemas import PaymentInfo
from service_clients import DJBCServiceClient
from orchestration import OrchestrationService

app = FastAPI()

# Initialize the DJBC service client
djbc_service_client = DJBCServiceClient(base_url="http://djbc-service")

# Initialize the orchestration service
orchestration_service = OrchestrationService(djbc_service_client)

@app.post("/submit-payment")
async def submit_payment(payment_info: PaymentInfo):
    try:
        payment_info_dict = payment_info.dict()
        response = orchestration_service.process_payment(payment_info_dict)
        return JSONResponse(content={"message": "Payment processed successfully", "response": response})
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
