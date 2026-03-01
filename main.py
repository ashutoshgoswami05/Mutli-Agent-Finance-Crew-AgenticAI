from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel,Field
from typing import Annotated
from agent import graph_application


app= FastAPI(title="Langraph Service")

class UserInput(BaseModel):
    Question: str = Field(title="Question you want to ask about your investment")
    Ticker: str = Field(title="Stock ticker you want to enquire about")


@app.post("/query",status_code=status.HTTP_200_OK)
async def getAnswer(userInput: UserInput):
    try:
        initial_state = {
            "ticker": userInput.Ticker, 
            "current_step": "supervisor",
            "question": userInput.Question
        }
        
        # Use ainvoke for non-blocking I/O
        answer = await graph_application.ainvoke(
            initial_state, 
            config={"recursion_limit": 10}
        )
        

        return {"status": "success", "data": answer.get("messages"), "format": "markdown"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Agent Error: {str(e)}")
