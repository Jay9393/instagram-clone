import json

from django.db.models.fields.json import JSONExact
from django.http                  import JsonResponse, request
from django.views                 import View

from posts.models                 import Comment, Post
from users.utils                  import ConfirmUser
from likes.models                 import Like

class PostLikeView(View):
    @ConfirmUser
    def post(self, request):
        data = json.loads(request.body)
        try:
            post_id = data["post_id"]
            post = Post.objects.get(id = post_id)
            already_like = Like.objects.filter(post=post_id).filter(user=request.user).exists()
            post_filter = Post.objects.filter(id=post.id)

            if not already_like:
                Like.objects.create(
                    post = post,
                    user = request.user,
                )
                post_filter.update(like_count=1)

            if already_like:
                post_count = Post.objects.get(id = post.id).like_count
                post_filter.update(like_count = post_count+1)

            if not data['post_id'] :
                raise ValueError

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )
            
        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

class CommentLikeView(View):
    @ConfirmUser
    def post(self, request):
        data = json.loads(request.body)
        try:
            comment_id = data["comment_id"]
            comment = Comment.objects.get(id = comment_id)
            already_like = Like.objects.filter(comment=comment_id).filter(user=request.user).exists()
            comment_filter = Comment.objects.filter(id=comment.id)

            if not already_like:

                Like.objects.create(
                    comment = comment,
                    user = request.user,
                )
                comment_filter.update(like_count=1)

            if already_like:
                comment_count = Comment.objects.get(id = comment.id).like_count
                comment_filter.update(like_count = comment_count+1)

            if not data['comment_id'] :
                raise ValueError
            
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )
            
        except KeyError :
            return JsonResponse({"message": "KEY ERROR"}, status=400 )
        
class PostUnLikeView(View):
    @ConfirmUser
    def post(self, request):
        data = json.loads(request.body)
        try:
            post_id = data["post_id"]
            post = Post.objects.get(id = post_id)
            post_filter = Post.objects.filter(id=post.id)

            if post.like_count:
                post_count = Post.objects.get(id = post.id).like_count
                post_filter.update(like_count = post_count-1)

            if not post.like_count:
                raise ValueError

            if not data['post_id'] :
                raise ValueError

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )
            
        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )


class CommentUnLikeView(View):
    @ConfirmUser
    def post(self, request):
        data = json.loads(request.body)
        try:
            comment_id = data["comment_id"]
            comment = Comment.objects.get(id = comment_id)
            comment_filter = Comment.objects.filter(id=comment.id)

            if comment.like_count:
                comment_count = Comment.objects.get(id = comment.id).like_count
                comment_filter.update(like_count = comment_count+1)

            if not comment.like_count:
                raise ValueError

            if not data['comment_id'] :
                raise ValueError
            
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )
            
        except KeyError :
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        # if data['post_id']:
        #     try:
                
            

        #     already_like = Like.objects.filter(post=data['post_id']).filter(user=request.user).exists() or Like.objects.filter(comment=data['comment_get']).filter(user=request.user.id).exists()
            

        #     # post, comment 둘다 날라오거나 둘다 없을 때 Value error
        #     if data['post_id'] and data['comment_id']:
        #         raise ValueError
            
        #     if not (data['post_id'] or data['comment_id']):
        #         raise ValueError

        #     if data['post_id']:
        #         global post_get
        #         
        #         global post_like
        #         post_like = Like.objects.filter(post=data['post_id'])
                

        #     if data['comment_id']:
        #         global comment_get
        #         comment_get = Comment.objects.get(id = data['comment_get'])
        #         global comment_like
        #         comment_like = Like.objects.filter(comment=data['comment_get'])

            

        #     # 기존에 like null 일 경우 생성
        #     if not already_like:
                # Like.objects.create(
                #     post = post_get,
                #     comment = comment_get,
                #     user = request.user,
                # )
        #         # post 일 경우
        #         if data['post_id']:
        #             Post.objects.filter(id=post_get.id).update(like_count=1)
        #         # comment 일 경우
        #         if data['comment_id']:
        #             Comment.objects.filter(id=post_get.id).update(like_count=1)

        #     else:
        #         return JsonResponse({"message": "INAPPROPRIATE LIKES"}, status=400 )

        #     # post like 있었을 경우    
        #     if post_like.exists():
        #         post_count = Like.objects.get(post = post_get.id).like_count
        #         Post.objects.filter(id = post_get.id).update(like_count = post_count+1)

        #     # comment_like 있었을 경우
        #     if comment_like.exists():
        #         comment_count = Like.objects.get(comment = comment_get.id).like_count
        #         Comment.objects.filter(id = comment_get.id).update(like_count = comment_count+1)
            
        #     return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        # except KeyError:
        #     return JsonResponse({"message": "KEY ERROR"}, status=400 )

        # except ValueError:
        #     return JsonResponse({"message": "VALUE ERROR"}, status=400 )

# class UNLikeView(View):
#     @ConfirmUser
#     def post(self, request):

#and data['comment_id']
#            print('===============================1=============================')