
# ---------------------------------------
# 1. 데이터 저장 공간
# ---------------------------------------

menus = [
    {
        "id": 1,
        "name": "짜장면",
        "calories": 650,
        "description": "춘장으로 만든 대표적인 중국 음식"
    },
    {
        "id": 2,
        "name": "짬뽕",
        "calories": 600,
        "description": "해산물과 채소를 넣은 얼큰한 국물 요리"
    },
    {
        "id": 3,
        "name": "탕수육",
        "calories": 800,
        "description": "바삭하게 튀긴 돼지고기에 새콤달콤한 소스를 곁들인 요리"
    }
]


next_id = 4


# ---------------------------------------
# 2. 전체 메뉴 조회
# ---------------------------------------

def get_all():
    print(menus)
    return menus


# ---------------------------------------
# 3. 메뉴 검색
# ---------------------------------------

def search(keyword):
    result = []
    for menu in menus:
        if keyword in menu["name"]:
            result.append(menu)

    # return [
    #     menu for menu in menus
    #     if keyword in menu["name"]
    # ]

    return result
# ---------------------------------------
# 4. 칼로리 검색
# ---------------------------------------

def search_calories(max_calories):
    result = []

    for menu in menus:

        if menu["calories"] <= max_calories:
            result.append(menu)

    # return [
    #     menu for menu in menus
    #     if menu["calories"] <= max_calories
    # ]

    return result
# ---------------------------------------
# 5. 특정 메뉴 조회
# ---------------------------------------

def get_one(menu_id):

    for menu in menus:
        if menu["id"] == menu_id:
            return menu

    return None


# ---------------------------------------
# 6. 메뉴 등록
# ---------------------------------------

def add(menu):

    global next_id

    new_menu = {
        "id": next_id,
        "name": menu["name"],
        "calories": menu["calories"],
        "description": menu["description"]
    }

    menus.append(new_menu)
    print('add',new_menu)
    next_id += 1

    return new_menu


# ---------------------------------------
# 7. 메뉴 수정
# ---------------------------------------

def update(menu_id, update_data):

    for menu in menus:

        if menu["id"] == menu_id:

            menu["name"] = update_data["name"]
            menu["calories"] = update_data["calories"]
            menu["description"] = update_data["description"]

            return menu

    return None


# ---------------------------------------
# 8. 메뉴 삭제
# ---------------------------------------

def delete(menu_id):

    for index, menu in enumerate(menus):

        if menu["id"] == menu_id:

            return menus.pop(index)
        

    return None
