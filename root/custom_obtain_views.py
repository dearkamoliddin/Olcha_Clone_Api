from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['success'] = True
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['username'] = self.user.username
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            refresh_token = RefreshToken(refresh_token)
            print(refresh_token)
            refresh_token.blacklist()
            response = {'Details': 'Successfully logged out.', 'refresh_token': str(refresh_token)}

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {'Details': 'Something went wrong.', 'more': str(e)}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
