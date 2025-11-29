from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import backend.langchain_helper as helper

app = FastAPI(title="AI Course Suggester API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenRequest(BaseModel):
    skills_known: str
    skills_want: str
    career_goal: str
    duration_months: int = 6

@app.post("/generate")
async def generate(req: GenRequest):
    try:
        out = helper.generate_course_plan(
            skills_known=req.skills_known,
            skills_want=req.skills_want,
            career_goal=req.career_goal,
            duration_months=req.duration_months,
        )
        return out
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
