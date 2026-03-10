from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel,Field
from typing import Annotated
from agent import graph_application
from pycircuitbreaker import circuit,CircuitBreakerError



app= FastAPI(title="Langraph Service")

class UserInput(BaseModel):
    Question: str = Field(title="Question you want to ask about your investment")
    Ticker: str = Field(title="Stock ticker you want to enquire about")

@circuit(failure_threshold=3,recovery_timeout=60)
async def call_the_graph_safely(initial_state):
    # Use ainvoke for non-blocking I/O
    answer=await graph_application.ainvoke(
            initial_state, 
            config={"recursion_limit": 10}
        )
    return answer 


@app.post("/query",status_code=status.HTTP_200_OK)
async def getAnswer(userInput: UserInput):
    try:
        initial_state = {
            "ticker": userInput.Ticker, 
            "current_step": "supervisor",
            "question": userInput.Question
        }
        

        answer = await call_the_graph_safely(initial_state)
         
        messages=answer.get("messages",[])

        return {"status": "success", "data": messages, "format": "markdown"}
    except CircuitBreakerError:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="The AI service is experiencing some difficulties please try again after 60s")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Agent Error: {str(e)}")
