from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class OnlyUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.username == self.kwargs["username"] or user.is_superuser
