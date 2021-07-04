import json

from django.db.models.fields.json import JSONExact
from django.http                  import JsonResponse, request
from django.views                 import View

from follows.models               import Follow
from users.utils                  import ConfirmUser
from users.models                 import User

class FollowView(View):
    @ConfirmUser
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            following = User.objects.get(id = data['following_id'])
            follower = User.objects.get(id = user.id)
            already_follow = Follow.objects.filter(user = user.id).filter(following = data['following_id']).exists()

            if following == follower:
                raise ValueError

            if  already_follow:
                raise ValueError

            Follow.objects.create(
                user = user,
                following = following,
            )

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201) 

        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )

class UnFollowView(View):
    @ConfirmUser
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            following = data['following_id']
            follower = request.user
            already_follow = Follow.objects.filter(user = user).filter(following = data['following_id']).exists()

            if following == follower:
                raise ValueError

            if not already_follow :
                raise ValueError

            Follow.objects.filter(user = user).filter(following = data['following_id']).delete()

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201) 

        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )
            
class GetFollowingView(View):
    @ConfirmUser
    def get(self, request):
        try:
            user = request.user
            followings = Follow.objects.filter(user = user.id)
            result = [{
                'nick_name' : f.following.nick_name,
                'name' : f.following.name,
            }for f in followings ]
            
            return JsonResponse({"result": result} , status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )

class GetFollowerView(View):
    @ConfirmUser
    def get(self, request):
        try:
            following = request.user
            followers = Follow.objects.filter(following_id = following.id)

            result = [{
                'nick_name' : f.user.nick_name,
                'name' : f.user.name,
            }for f in followers ]
            
            return JsonResponse({"result": result} , status=201)
        
        except KeyError:
            return JsonResponse({"message": "KEY ERROR"}, status=400 )

        except ValueError:
            return JsonResponse({"message": "VALUE ERROR"}, status=400 )