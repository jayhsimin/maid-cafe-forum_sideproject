# 導入Django的path函數和視圖模組
from django.urls import path
from . import views  # 導入當前目錄下的views模組

# 定義應用程式命名空間(防止不同app間的URL名稱衝突)
app_name = 'maid_cafe'  # 這個應用的所有URL名稱都會帶有'maid_cafe:'前綴

# URL路由配置列表
urlpatterns = [
    # 首頁URL
    # - 空路徑('')對應網站根目錄
    # - 使用views.home處理請求
    # - 命名為'home'，在模板中使用{% url 'maid_cafe:home' %}
    path('', views.home, name='home'),
    
    # 女僕咖啡店列表頁
    # - 路徑'maid-cafes/'
    # - 使用views.maid_cafe_list視圖函數
    # - 命名為'maid_cafe_list'
    path('maid-cafes/', views.maid_cafe_list, name='maid_cafe_list'),
    
    # 女僕咖啡店詳細頁
    # - 路徑'maid-cafes/<int:pk>/'包含整數參數pk
    # - <int:pk>表示捕獲URL中的整數作為主鍵參數
    # - 使用views.maid_cafe_detail視圖函數
    # - 命名為'maid_cafe_detail'
    path('maid-cafes/<int:pk>/', views.maid_cafe_detail, name='maid_cafe_detail'),
    
    # 以下是各種論壇子頁面的URL配置
    # 所有路徑使用kebab-case命名約定(單詞間用連字符連接)
    
    # 女僕店論壇頁面
    path('maid-cafe-forum/', views.maid_cafe_forum, name='maid_cafe_forum_page'),
    
    # 女僕論壇頁面
    path('maid-forum/', views.maid_forum, name='maid_forum_page'),
    
    # 動漫論壇頁面
    path('anime-forum/', views.anime_forum, name='anime_forum_page'),
    
    # 女僕八卦頁面
    path('gossip-maid/', views.gossip_maid, name='gossip_maid_page'),
    
    # 女僕店八卦頁面
    path('gossip-cafe/', views.gossip_cafe, name='gossip_cafe_page'),
    
    # 奧客專區頁面
    path('troublemaker-zone/', views.troublemaker_zone, name='troublemaker_zone_page'),
    
    # 名人堂頁面
    path('hall-of-fame/', views.hall_of_fame, name='hall_of_fame_page'),
    
    # 女僕排行頁面
    path('maid-ranking/', views.maid_ranking, name='maid_ranking_page'),
    
]