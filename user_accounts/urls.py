'''
Accounts urls configuration
'''

# Import all requirements
from django.urls import path
from allauth.account.views import LogoutView, PasswordSetView, PasswordChangeView, PasswordResetView
from .views import login_signup, CusLoginView, CusSignupView, dashboardView, update_user
from .backends import update_user as UPDATE_DETAIL, costomer_detail, add_comment, like

urlpatterns = [
    path('', login_signup, name='login_or_signup'),
    path('dashboard', dashboardView, name='dashboard'),
    path('login/', CusLoginView.as_view(), name='login'),
    path('signup/', CusSignupView.as_view(), name='signup'),
    path('address', costomer_detail, name='address'),
    path('comment/add', add_comment, name='add_comment'),
    path('update_detail', UPDATE_DETAIL, name="update_detail"),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('set_password/', PasswordSetView.as_view(), name='set_password'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('rest_password/', PasswordResetView.as_view(), name='rest_password'),
    path('like', like, name='like'),
    #path('social/', ConnectionsView.as_view(), name='social'),
]
