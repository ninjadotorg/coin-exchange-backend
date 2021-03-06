from django.urls import path, include
from rest_framework.routers import DefaultRouter

from coin_user.resource import ContactViewSet, ExchangeUserLogViewSet
from coin_user.views import SignUpView, ProfileView, VerifyEmailView, WalletView, VerifyPhoneView, VerifyIDView, \
    VerifySelfieView, ForgotPasswordView, ChangePasswordView, ResetPasswordView, TwoFAView, \
    ReferralView, FileUploadView, VerifyPasswordView, APITokenView

router = DefaultRouter()
router.register('contacts', ContactViewSet)
router.register('logs', ExchangeUserLogViewSet)

patterns = ([
    path('', include(router.urls)),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('referrals/', ReferralView.as_view(), name='referrals'),
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('verify-phone/', VerifyPhoneView.as_view(), name='verify-phone'),
    path('verify-id/', VerifyIDView.as_view(), name='verify-id'),
    path('verify-selfie/', VerifySelfieView.as_view(), name='verify-selfie'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('verify-password/', VerifyPasswordView.as_view(), name='verify-password'),
    path('two-fa/', TwoFAView.as_view(), name='two-fa'),
    path('file-upload/', FileUploadView.as_view(), name='file-upload-view'),
    path('api-token/', APITokenView.as_view(), name='api-token-view'),
], 'user')

urlpatterns = [
    path('user/', include(patterns)),
]
