from fastapi import FastAPI, HTTPException, Response
from app.pdf_to_text import openaiCompletionApi
import os

app = FastAPI()

#test route example
@app.get("/course_plan/", tags=['courseplanAPI'])
async def courseplanAPI(url: str = ""):
    if url == "":
        raise HTTPException(status_code=400, detail="please insert an url to pdf file")
    md_name = openaiCompletionApi(url)
    f = open(md_name, "r").read()
    os.remove(md_name)
    return Response(content=f, media_type="text/markdown")
    
