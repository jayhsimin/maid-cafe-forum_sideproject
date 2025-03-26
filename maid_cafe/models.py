# 導入Django的models模組
from django.db import models

# 女僕咖啡店模型
class MaidCafe(models.Model):
    """
    女僕咖啡店資料模型
    包含咖啡店基本資訊和圖片
    """
    
    # 咖啡店名稱欄位
    # CharField用於存儲較短的字串
    # max_length=255 限制最大長度為255字符
    name = models.CharField(max_length=255, verbose_name="咖啡店名稱")
    
    # 咖啡店描述欄位
    # TextField用於存儲較長的文字內容
    description = models.TextField(verbose_name="描述")
    
    # 咖啡店位置欄位
    location = models.CharField(max_length=255, verbose_name="位置")
    
    # 咖啡店圖片欄位
    # ImageField用於上傳圖片
    # upload_to='maid_cafes/' 指定圖片上傳目錄
    # null=True 允許資料庫中存儲NULL值
    # blank=True 允許表單提交時為空值
    image = models.ImageField(
        upload_to='maid_cafes/', 
        null=True, 
        blank=True,
        verbose_name="咖啡店圖片"
    )

    # 定義物件的字串表示方法
    # 在Django管理後台和shell中顯示用
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "女僕咖啡店"  # 單數名稱
        verbose_name_plural = "女僕咖啡店"  # 複數名稱

# 女僕模型
class Maid(models.Model):
    """
    女僕資料模型
    包含女僕基本資訊、所屬咖啡店和圖片
    """
    
    # 女僕名稱欄位
    name = models.CharField(max_length=255, verbose_name="女僕名稱")
    
    # 女僕描述欄位
    description = models.TextField(verbose_name="描述")
    
    # 所屬咖啡店關聯欄位
    # ForeignKey建立多對一關係(一個女僕屬於一家咖啡店，一家咖啡店有多個女僕)
    # on_delete=models.CASCADE 表示當咖啡店被刪除時，相關女僕也會被刪除
    # related_name='maids' 允許從咖啡店反向查詢所屬女僕
    cafe = models.ForeignKey(
        MaidCafe,
        on_delete=models.CASCADE,
        related_name='maids',
        verbose_name="所屬咖啡店"
    )
    
    # 女僕圖片欄位
    image = models.ImageField(
        upload_to='maids/', 
        null=True, 
        blank=True,
        verbose_name="女僕圖片"
    )

    # 定義物件的字串表示方法
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "女僕"  # 單數名稱
        verbose_name_plural = "女僕"  # 複數名稱