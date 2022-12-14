from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact_view, name="contact_view"),
    path('airlift/', airlift, name="airlift"),
    path('wildearth/', wildearth, name="wildearth"),

    path('blogs/', home, name="home"),
    path('login-for-admin-only/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('add-blog/', add_blog, name="add_blog"),
    path('blog-detail/<slug>', blog_detail, name="blog_detail"),
    path('see-blog/', see_blog, name="see_blog"),
    path('blog-delete/<id>', blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', blog_update, name="blog_update"),

    path('career/', career, name="career"),
    path('add-job/', add_job, name="add_job"),
    path('job-detail/<slug>', job_detail, name="job_detail"),
    path('see-job/', see_job, name="see_job"),
    path('job-delete/<id>', job_delete, name="job_delete"),
    path('job-update/<slug>/', job_update, name="job_update"),

    path('logout-view/', logout_view, name="logout_view"),
    path('verify/<token>/', verify, name="verify")
]
