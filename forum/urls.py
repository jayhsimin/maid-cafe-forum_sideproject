from django.urls import path  # 匯入 path 函式，用於定義 URL 路由
from . import views  # 匯入當前應用的 views 模組（處理請求的函式）

# 設定應用命名空間，確保 URL 反解析時不會與其他應用的 URL 衝突
app_name = 'forum'  # 必须添加這行，讓 {% url 'forum:post_list' %} 這樣的寫法可用

# 定義 URL 模式（urlpatterns）
urlpatterns = [
    path('', views.post_list, name='post_list'),  
    # 當用戶訪問 "forum/" 時，執行 views.post_list，顯示文章列表
    # 這個視圖通常會傳遞 `posts` 變數到模板中，顯示所有文章的標題與連結

    path('<int:pk>/', views.post_detail, name='post_detail'),  
    # 當用戶訪問 "forum/<文章ID>/" 時，執行 views.post_detail，顯示特定文章詳情
    # 例如，訪問 "forum/3/" 會調用 `post_detail(request, pk=3)`，顯示 ID 為 3 的文章
]
