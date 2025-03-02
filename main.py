from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks
STUDENT_MARKS_FILE = "marks.csv"
students = {}

with open(STUDENT_MARKS_FILE, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row["name"]] = int(row["marks"])

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    return {"marks": [students[n] for n in name if n in students]}
