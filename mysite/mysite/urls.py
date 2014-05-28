from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'project_manager.views.landing'),
    url(r'^sales_home/', 'project_manager.views.sales_home'),
    url(r'^manager_home/', 'project_manager.views.manager_home'),
    url(r'^artist_home/', 'project_manager.views.artist_home'),
    url(r'^sales_manager_home/', 'project_manager.views.sales_manager_home'),
    url(r'^create_project/', 'project_manager.views.create_project'),
    url(r'^edit_project/', 'project_manager.views.edit_project'),
    url(r'^edit_line/', 'project_manager.views.edit_line'),
    url(r'^view_project/', 'project_manager.views.view_project'),
    url(r'^allocated_projects/', 'project_manager.views.allocated_projects'),
    url(r'^go_home/', 'project_manager.views.go_home'),
    url(r'^logout/','project_manager.views.logout')
)
