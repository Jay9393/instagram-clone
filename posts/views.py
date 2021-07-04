import json

from django.db.models.fields.json import JSONExact
from django.http                  import JsonResponse, request
from django.views                 import View

from posts.models                 import Comment, Post
from users.utils                  import ConfirmUser

class PostView(View):
    @ConfirmUser
    def post(self, request):
        data = json.loads(request.body)
        print(request.user)
        Post.objects.create(
            img     = data['img'],
            content = data['content'],
            user    = request.user,
        )

        return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)
        
    def get(self, request):
        posts   = Post.objects.all()
    
        result = [{
            "user"      : post.user.nick_name,
            "img"       : post.img,
            "content"   : post.content,
            "created_at": post.created_at,
        } for post in posts]

        return JsonResponse({"result" : result}, status=200)


class CommentPost(View):
    @ConfirmUser
    def post(self, request):
        data = json.loads(request.body)
        post    = Post.objects.get(id=data["post_id"])
        
        Comment.objects.create(
            content = data["content"],
            post    = post,
            users   = request.user,
        )

        return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

class CommentView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            comments     = Post.objects.get(id=data['post_id']).main_comments.all()

            result = [{
                "content"         : comment.content,
                "user"            : comment.users.nick_name,
                "created_at"      : comment.created_at,
                "updated_at"      : comment.updated_at,
            } for comment in comments]

            return JsonResponse({"result": result}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )


class NestedPost(View):
    @ConfirmUser
    def post(slef, request):
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id=data["post_id"])
            comment = Comment.objects.get(id=data["comment_id"])

            Comment.objects.create(
                content = data["content"],
                post    = post,
                comment = comment,
                users   = request.user
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )


class NestedView(View):
    def post(self, request):
        data = json.loads(request.body)
        nested_comments     = Comment.objects.get(id=data['comment_id']).nested_comments.all()

        result = [{
            "content"         : comment.content,
            "user"            : comment.users.nick_name,
            "created_at"      : comment.created_at,
            "updated_at"      : comment.updated_at,
        } for comment in nested_comments]

        return JsonResponse({"result": result}, status=201)
    