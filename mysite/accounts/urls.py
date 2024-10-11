from django.urls import include, path
from accounts.views import (
    AccountCreationForm,
    profile,
    edit_profile,
    all_users,
    search_users,
)

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", AccountCreationForm.as_view(), name="accounts.register"),
    path("profile", profile, name="accounts.profile"),
    path("profile/update", edit_profile, name="accounts.update"),
    path("users", all_users, name="accounts.users"),
    path("search/", search_users, name="accounts.search"),
]
