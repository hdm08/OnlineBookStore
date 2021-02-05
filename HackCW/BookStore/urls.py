from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.Home, name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name="logout"),

    path('dashboard/', views.Dashboard, name="dashboard"),

    # path('profile/', views.Profile, name="profile"),
    path('sellbook/', views.SellBook, name="sellbook"),
    path('donatebook/', views.DonateBook, name="donatebook"),

    path('sellbook/<int:id>', views.SellBook, name="updatesellbook"),
    path('donatebook/<int:id>', views.DonateBook, name="updatedonatebook"),

    path('delete/<int:id>/', views.Book_Delete, name='book_delete'),


    path('sellbookhistory/', views.SellBookHistory, name="sellbookhistory"),
    path('donatebookhistory/', views.DonateBookHistory, name="donatebookhistory"),

    path('buybookview/', views.BuyBookView, name="media"),
    path('freebookview/', views.FreeBookView, name="freebook"),

    # path('media/', views.Buy, name="media"),
    path('testimonial/', views.Testimonial, name="testimonial"),
    path('ChangePassword', views.ChangePassword, name="ChangePassword"),

    path('order/', views.Order, name="order"),
    # path('pay/', views.PaymentPage, name="pay"),

    path('done/', views.Done, name="done"),

    path('cart/', views.Cart, name="cart"),
    path('checkout/', views.Checkout, name="checkout"),
    path('contact/', views.Contact, name="contact"),
    path('about/', views.About, name="about"),
    path('p_detail/<int:myid>', views.P_detail, name="p_detail"),
    path('blog/', views.Blog, name="blog"),
    # path('history/', views.History, name="history"),
    path('cart/', views.Cart, name='cart'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reset/password_reset.html',
             subject_template_name='reset/password_reset_subject.txt',
             email_template_name='reset/password_reset_email.html',
             success_url='done'
         ),name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='reset/password_reset_done.html'
         ),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reset/password_reset_confirm.html'
         ),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='reset/password_reset_complete.html'
         ),name='password_reset_complete'),

]