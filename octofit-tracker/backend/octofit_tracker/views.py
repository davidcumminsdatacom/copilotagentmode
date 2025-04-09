from django.http import JsonResponse

# Updated viewsets to include the corrected codespace URL in responses
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['codespace_url'] = 'https://laughing-funicular-x59g76gq44jqhq7x-8000.app.github.dev'
        return JsonResponse(response.data)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['codespace_url'] = 'https://laughing-funicular-x59g76gq44jqhq7x-8000.app.github.dev'
        return JsonResponse(response.data)

# Similar updates can be applied to other viewsets if needed.