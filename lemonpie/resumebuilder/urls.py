from django.conf.urls import url

from . import views

app_name = 'resumebuilder'
urlpatterns = [
    url(r'^groups/$', views.AllGroupsView.as_view(), name='all_groups'),
    url(r'^groups/add/$', views.add_new_group, name='add_new_group'),
    url(r'^groups/(?P<group_id>[0-9]+)/$', views.group_view, name='group_view'),
    url(r'^groups/(?P<group_id>[0-9]+)/delete/$', views.delete_group, name='delete_group'),
    url(r'^resumes/$', views.AllCVsView.as_view(), name='all_cvs'),
    url(r'^resumes/(?P<cv_id>[0-9]+)/$', views.cv_view, name='cv_view'),
    url(r'^resumes/(?P<cv_id>[0-9]+)/modify/$', views.modify_cv, name='modify_cv'),
    url(r'^resumes/add/$', views.add_new_cv, name='add_new_cv'),
    url(r'^resumes/(?P<cv_id>[0-9]+)/delete/$', views.delete_cv, name='delete_cv'),
    url(r'^resumes/(?P<cv_id>[0-9]+)/add_group/$', views.add_group_cv, name='add_group_cv'),
    url(r'^resumes/(?P<cv_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/delete_group/$', views.delete_group_from_cv, name='delete_group_from_cv'),
]
