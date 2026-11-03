// data.js
//const API_BASE_URL = "http://192.168.0.5:8000";
const API_BASE_URL = "";

// 전체 메뉴 조회
async function getAllMenus() {
    try {
        const response = await fetch(`${API_BASE_URL}/menus`);
        if (!response.ok) throw new Error("전체 메뉴를 불러오지 못했습니다.");
        return await response.json();
    } catch (error) {
        console.error(error);
        return [];
    }
}

// 메뉴 검색 (백엔드 /menus/search 활용)
async function searchMenus(keyword = "") {
    try {
        const response = await fetch(`${API_BASE_URL}/menus/search?keyword=${encodeURIComponent(keyword)}`);
        if (!response.ok) throw new Error("메뉴 검색에 실패했습니다.");
        return await response.json();
    } catch (error) {
        console.error(error);
        return [];
    }
}

// 특정 메뉴 조회
async function getMenu(menuId) {
    try {
        const response = await fetch(`${API_BASE_URL}/menus/${menuId}`);
        if (!response.ok) throw new Error("메뉴를 찾을 수 없습니다.");
        return await response.json();
    } catch (error) {
        console.error(error);
        return null;
    }
}

// 메뉴 등록
async function addMenu(menuData) {
    try {
        const response = await fetch(`${API_BASE_URL}/menus`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(menuData),
        });
        if (!response.ok) throw new Error("메뉴 등록에 실패했습니다.");
        return await response.json();
    } catch (error) {
        console.error(error);
        alert("메뉴 등록 중 오류가 발생했습니다.");
    }
}

// 메뉴 수정
async function updateMenu(menuId, menuData) {
    try {
        const response = await fetch(`${API_BASE_URL}/menus/${menuId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(menuData),
        });
        if (!response.ok) throw new Error("메뉴 수정에 실패했습니다.");
        return await response.json();
    } catch (error) {
        console.error(error);
        alert("메뉴 수정 중 오류가 발생했습니다.");
    }
}

// 메뉴 삭제
async function deleteMenu(menuId) {
    try {
        const response = await fetch(`${API_BASE_URL}/menus/${menuId}`, {
            method: "DELETE",
        });
        if (!response.ok) throw new Error("메뉴 삭제에 실패했습니다.");
        return await response.json();
    } catch (error) {
        console.error(error);
        alert("메뉴 삭제 중 오류가 발생했습니다.");
    }
}