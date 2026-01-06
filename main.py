import os
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
#configure .env file
load_dotenv()
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"]
)
#static files 
app.mount("/static", StaticFiles(directory="static"), name="static")

generative_config = {
    "temperature": 1.2,
    "max_output_tokens": 50
}
# genai config
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest",
generation_config=generative_config)
@app.post("/")
async def quote_generate():
    try:
        prompt = ("What is python?")
        res = model.generate_content(prompt)
        if not res:
            raise ValueError("the result is empty")
        return {"quote":res.text}
    except Exception  as e:
        raise HTTPException(status_code=500,detail=str(e))