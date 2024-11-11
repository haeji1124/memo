from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()


class Memo(BaseModel):
    id: str
    content: str


memos = []


@app.get("/memos")
def read_memo():
    return memos


@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return '메모 추가에 성공했습니다.'


@app.put("/memos/{memo_id}")
def edit_memo(req_memo: Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '메모 수정을 성공했습니다.'

    return f'{req_memo.id}의 메모는 없습니다.'


app.mount("/", StaticFiles(directory="static", html=True), name="static")
