from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from main.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/info/', InfoView.as_view()),
    path('api/blog/', BlogView.as_view()),
    path('api/game/', GameView.as_view()),
    path('api/user/', UserView.as_view()),
    path('api/photo/', PhotoView.as_view()),
    path('api/number/', NumberView.as_view()),
    path('api/email/', EmailView.as_view()),
    path("api/competition/",CompetitionView.as_view()),
    # path('api/random/<int:pk>/', Random_Competition.as_view()),f
    path("home/", Admin_Home, name='home'),
    path("game/<int:pk>/", Admin_Game, name='game'),
    path("start/<int:pk>/", Admin_Start, name='start'),
    path("start_game/<int:pk>/",Admin_Start_Game,name="start_game"),
    path("dis_active/<int:pk>/",Admin_Dis_Active,name="dis_active"),
    path("", Login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
