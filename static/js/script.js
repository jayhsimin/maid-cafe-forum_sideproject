// 示例：在控制台輸出歡迎訊息
console.log("Welcome to Maid Cafe Forum!");

// 示例：為導航欄添加動態效果
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('mouseover', () => {
        link.style.color = '#ff6347'; // 鼠標懸停時改變顏色
    });

    link.addEventListener('mouseout', () => {
        link.style.color = 'white'; // 鼠標離開時恢復顏色
    });
});