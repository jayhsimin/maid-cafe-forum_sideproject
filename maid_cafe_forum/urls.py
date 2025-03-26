# 導入Django內建管理後台模組
from django.contrib import admin
# 導入Django URL路由相關函式
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 定義專案的URL路由配置列表
urlpatterns = [
    # 管理後台URL配置
    # - 'admin/' 是後台的訪問路徑
    # - admin.site.urls 提供Django內建的管理界面
    path('admin/', admin.site.urls),
    
    # 主應用程式路由配置
    # - 空路徑('')表示網站根目錄
    # - 包含maid_cafe應用程式的URLs配置
    # - namespace='maid_cafe' 為URL命名空間，避免不同app間的URL名稱衝突
    path('', include('maid_cafe.urls', namespace='maid_cafe')),
    
    # 論壇應用程式路由配置
    # - 'forum/' 前綴表示所有論壇相關URL都以此開頭
    # - 包含forum應用程式的URLs配置
    # - 使用元組格式 (app_name, namespace) 明確指定應用程式名稱和命名空間
    # - namespace='forum' 為論壇URL設置命名空間
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),

    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)