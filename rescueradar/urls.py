from django.urls import include, path
from django.contrib import admin
from base import views as base_views
from base.views import request_submitted
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', base_views.home, name='home'),
    path('about/', base_views.about, name='about'),
    path('contact/', base_views.contact, name='contact'),
    path('accounts/profile/', base_views.profile, name='profile'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    path('error_message/', base_views.error_message, name='error_message'),
    path('all_agencies/', base_views.all_agencies, name='all_agencies'),
    path('request_submitted/<str:form_submitted>/', base_views.request_submitted, name='request_submitted'),
    path('user_profile/', base_views.user_profile, name='user_profile'),
    path('user_report/', base_views.user_report, name='user_report'),
    path('rooms/', base_views.rooms, name='rooms'),
    path('victims_portal/', base_views.victims_portal, name='victims_portal'),
    path('chatroom/',base_views.chatroom, name='chatroom'),
    # path('chatroom/',base_views.senddata_to_flask, name='senddata_to_flask'),
    path('profileEdit/',base_views.profileEdit, name='profileEdit'),
    path('agencyPage/',base_views.agencyPage, name='agencyPage'),
    path('post/<int:pk>/', base_views.post_detail, name='post_detail'),
    path('post/new/', base_views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', base_views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', base_views.post_delete, name='post_delete'),
    path('display-map/', base_views.display_map, name='display_map'),
    path('sam/', base_views.display_ip_info, name='sam'),
    path('emergency/', base_views.emergency_report, name='user_report'),
    # path('bb',base_views.faild,name='failed'),
    path('bb',base_views.Chatbot,name='Chatbot'),
    path('ab',base_views.victims_portal_s,name='victimportaldetailed'),
    path('bc',base_views.approve,name='Approving_agency'),
    path('agency_approved/<str:id>',base_views.agency_approved,name='agency_approved'),
    


    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]