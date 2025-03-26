from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'forum/post_list.html', {'posts': posts})

# 修改：添加留言表單處理
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:  # 確保用戶已登入
            Comment.objects.create(post=post, author=request.user, content=content)
            return redirect('forum:post_detail', pk=pk)
    return render(request, 'forum/post_detail.html', {'post': post})