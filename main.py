
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from storage import data
from fastapi.responses import HTMLResponse

app = FastAPI()


# ---------------------------------------
# CORS 설정
# ---------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------
# 데이터 형식 정의
# ---------------------------------------

class Menu(BaseModel):
    name: str
    calories: int
    description: str


# ---------------------------------------
# READ : 전체 메뉴 조회
# ---------------------------------------

@app.get("/menus")
def get_menus():
    return data.get_all()


# ---------------------------------------
# READ : 메뉴 검색
# ---------------------------------------

@app.get("/menus/search")
def search_menu(keyword: str = ""):
    return data.search(keyword)


# ---------------------------------------
# READ : 칼로리 검색
# ---------------------------------------

@app.get("/menus/calories")
def search_calories(max_calories: int):
    return data.search_calories(max_calories)


# ---------------------------------------
# READ : 특정 메뉴 조회
# ---------------------------------------

@app.get("/menus/{menu_id}")
def get_menu(menu_id: int):

    menu = data.get_one(menu_id)

    if menu is None:
        raise HTTPException(404, "메뉴를 찾을 수 없습니다.")

    return menu


# ---------------------------------------
# CREATE : 메뉴 등록
# ---------------------------------------

@app.post("/menus")
def add_menu(menu: Menu):

    new_menu = data.add(menu.model_dump())

    return {
        "message": "메뉴 등록 성공",
        "data": new_menu
    }


# ---------------------------------------
# UPDATE : 메뉴 수정
# ---------------------------------------

@app.put("/menus/{menu_id}")
def update_menu(menu_id: int, update_data: Menu):

    updated = data.update(menu_id, update_data.model_dump())

    if updated is None:
        raise HTTPException(404, "수정할 메뉴를 찾을 수 없습니다.")

    return {
        "message": "메뉴 수정 성공",
        "data": updated
    }


# ---------------------------------------
# DELETE : 메뉴 삭제
# ---------------------------------------

@app.delete("/menus/{menu_id}")
def delete_menu(menu_id: int):

    deleted = data.delete(menu_id)

    if deleted is None:
        raise HTTPException(404, "삭제할 메뉴를 찾을 수 없습니다.")

    return {
        "message": "메뉴 삭제 성공",
        "data": deleted
    }



@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", encoding='utf-8') as f:
        return f.read()