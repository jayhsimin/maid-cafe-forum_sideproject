# 導入Django快捷渲染函式和模型
from django.shortcuts import render
from .models import MaidCafe  # 導入女僕咖啡店模型
from forum.models import Post

# 首頁視圖函式
def home(request):
    """
    處理網站首頁請求
    獲取所有女僕咖啡店資料並渲染首頁模板
    """
    cafes = MaidCafe.objects.all()  # 從資料庫獲取所有女僕店記錄
    return render(request, 'home.html', {'cafes': cafes})  # 渲染模板並傳遞資料

# 女僕咖啡店列表視圖
def maid_cafe_list(request):
    """
    顯示所有女僕咖啡店列表
    使用與首頁相同的資料但渲染不同模板
    """
    cafes = MaidCafe.objects.all()  # 查詢所有女僕店
    return render(request, 'maid_cafe/list.html', {'cafes': cafes})  # 傳遞到列表模板

# 女僕咖啡店詳細資訊視圖
def maid_cafe_detail(request, pk):
    """
    顯示單個女僕咖啡店詳細資訊
    :param pk: 主鍵參數，用於識別特定女僕店
    """
    cafe = MaidCafe.objects.get(pk=pk)  # 根據主鍵獲取單一記錄
    return render(request, 'maid_cafe/detail.html', {'cafe': cafe})  # 傳遞單一店鋪資料

# 以下是各類論壇子頁面的視圖函式
# 使用相同的模板但傳遞不同的標籤參數

def maid_cafe_forum(request):
    """女僕咖啡店討論區視圖"""
    return render(request, 'maid_cafe/maid_cafe_forum.html', {'label': '女僕店論壇'})

def maid_forum(request):
    """女僕從業人員討論區視圖"""
    return render(request, 'maid_cafe/maid_forum.html', {'label': '女僕論壇'})

def anime_forum(request):
    """動漫相關討論區視圖"""
    return render(request, 'maid_cafe/anime_forum.html', {'label': '動漫論壇'})

def gossip_maid(request):
    """女僕八卦話題視圖"""
    return render(request, 'maid_cafe/gossip_maid.html', {'label': '八卦女僕'})

def gossip_cafe(request):
    """咖啡店八卦話題視圖"""
    return render(request, 'maid_cafe/gossip_cafe.html', {'label': '八卦女僕店'})

def troublemaker_zone(request):
    """奧客討論專區視圖"""
    return render(request, 'maid_cafe/troublemaker_zone.html', {'label': '奧客專區'})

def hall_of_fame(request):
    """名人堂展示視圖"""
    return render(request, 'maid_cafe/hall_of_fame.html', {'label': '名人堂'})

def maid_ranking(request):
    """女僕排名系統視圖"""
    return render(request, 'maid_cafe/maid_ranking.html', {'label': '女僕排行'})

