# backend/langchain_helper.py
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from backend.secret_key import groq_api_key
import random, json

# Initialize LLM with Groq key
llm = ChatGroq(
    temperature=0.6,
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant",
)

parser = StrOutputParser()

# Strict JSON prompt (escaped)
prompt_json = PromptTemplate(
    input_variables=["skills_known", "skills_want", "career_goal", "duration_months", "seed"],
    template=(
        "You are an expert career mentor.\n"
        "Input:\n"
        "Skills known: {skills_known}\n"
        "Skills to learn: {skills_want}\n"
        "Career goal: {career_goal}\n"
        "Duration months: {duration_months}\n"
        "Seed: {seed}\n\n"

        "Return a STRICT JSON object:\n\n"

        "{{\n"
        "  \"courses\": [\n"
        "    {{\"title\": \"Intro to X\", \"objective\": \"Learn basics\", \"platforms\": [\"YouTube\", \"Coursera\", \"Udemy\"]}},\n"
        "    ...\n"
        "  ],\n"
        "  \"roadmap\": {{\"phase1\": \"Fundamentals\", \"phase2\": \"Projects\", \"phase3\": \"Portfolio\"}},\n"
        "  \"notes\": \"Short tip\"\n"
        "}}\n\n"

        "Return ONLY JSON. No comments."
    )
)

def generate_course_plan(skills_known, skills_want, career_goal, duration_months=6):
    seed = random.randint(1000, 9999)

    prompt_input = {
        "skills_known": skills_known,
        "skills_want": skills_want,
        "career_goal": career_goal,
        "duration_months": duration_months,
        "seed": seed,
    }

    raw = (prompt_json | llm | parser).invoke(prompt_input).strip()

    try:
        parsed = json.loads(raw)
        return {"success": True, "data": parsed, "raw": raw}
    except Exception as e:
        return {"success": False, "raw": raw, "error": str(e)}
