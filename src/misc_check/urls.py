from django.urls import path, include

from misc_check.views import ProtectedView, PublicView

patterns = ([
    path('protected-view', ProtectedView.as_view(), name='protected-view'),
    path('public-view', PublicView.as_view(), name='public-view'),
], 'misc_check')

urlpatterns = [
    path('misc-check/', include(patterns)),
]
