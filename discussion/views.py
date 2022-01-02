from django.shortcuts import render
from .models import Post, Reply
from user_profile.models import Profile


# Create your views here.
def forum(request):
    profile = Profile.objects.all()

    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count

    post_count = request.session.get('post_count', 0)

    if request.method == "POST":
        user = request.user
        image = request.user.profile.image
        content = request.POST.get('content', '')
        title = request.POST.get('title', '')
        post = Post(user1=user, title=title, post_content=content, image=image)
        post.save()
        posts = Post.objects.filter(admin_approved=True).order_by('-date_added')
        alert = True

        post_count += 1
        request.session['post_count'] = post_count

        return render(request, "chat/forum.html",
                      {
                          'alert': alert,
                          'current_post': post,
                          'posts': posts,
                          'visit_count': visit_count,
                          'post_count': post_count,
                          'reply_count': request.session.get('reply_count', 0),
                      })
    posts = Post.objects.filter(admin_approved=True).order_by('-date_added')
    return render(request, "chat/forum.html", {'posts': posts,
                                               'visit_count': visit_count,
                                               'post_count': post_count,
                                               'reply_count': request.session.get('reply_count', 0),
                                               })


def discussion(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    replies = Reply.objects.filter(post=post)
    if request.method == "POST":
        user = request.user
        if 'rate-button' in request.POST and user == post.user:
            reply_id = request.POST.get('reply_id', '')
            reply = Reply.objects.filter(id=reply_id).first()
            reply.rate = request.POST.get('rate', 1)
            reply.save()
            replies = Reply.objects.filter(post=post)
            return render(request, "chat/discussion.html",
                          {
                              'username': user.username,
                              'post': post,
                              'replies': replies,
                          })
        elif 'reply-submit' in request.POST:
            image = request.user.profile.image
            desc = request.POST.get('desc', '')
            post_id = request.POST.get('post_id', '')
            reply = Reply(user=user, reply_content=desc, post=post, image=image)
            reply.save()
            replies = Reply.objects.filter(post=post)
            alert = True

            reply_count = request.session.get('reply_count', 0)
            request.session['reply_count'] = reply_count + 1

            return render(request, "chat/discussion.html",
                          {
                              'username': user.username,
                              'post': post,
                              'replies': replies,
                              'alert': alert
                          })
    return render(request, "chat/discussion.html",
                  {
                      'post': post,
                      'replies': replies
                  })
