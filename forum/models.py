from django.db import models  # 匯入 Django 的 ORM 模型功能
from django.contrib.auth.models import User  # 匯入 Django 內建的 User 模型，代表使用者

# 定義文章（Post）模型
class Post(models.Model):
    title = models.CharField(max_length=255)  # 文章標題，字元上限 255
    content = models.TextField()  # 文章內容，無長度限制
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    # 作者，關聯 Django 內建的 User 模型
    # on_delete=models.CASCADE 代表當使用者被刪除時，該使用者的文章也會一併刪除

    created_at = models.DateTimeField(auto_now_add=True)  
    # 文章建立時間，auto_now_add=True 表示第一次建立時自動填入時間

    updated_at = models.DateTimeField(auto_now=True)  
    # 文章最後更新時間，auto_now=True 表示每次更新時自動填入時間

    def __str__(self):
        return self.title  # 定義模型的字串表示，返回文章標題

# 定義留言（Comment）模型
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    # 關聯文章（Post），一篇文章可以有多則留言
    # related_name='comments' 讓 Post 物件可以透過 post.comments 來取得所有留言
    # on_delete=models.CASCADE 代表當文章被刪除時，相關的留言也會刪除

    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    # 作者，關聯 Django 內建的 User 模型
    # 當使用者被刪除時，該使用者發表的留言也會刪除

    content = models.TextField()  # 留言內容，無長度限制
    created_at = models.DateTimeField(auto_now_add=True)  
    # 留言時間，第一次建立時自動填入時間

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'  
    # 定義模型的字串表示，顯示留言者與對應的文章標題
