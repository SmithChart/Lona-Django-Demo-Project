from __future__ import annotations

from lona.html import HTML
from lona.view import LonaView
from lona_picocss.html import H1, TextInput, Button, Ul, Li

from lona_project.database.models import (
    Demo,
)


class HomeView(LonaView):
    DJANGO_AUTH_LOGIN_REQUIRED = True

    def handle_btn(self, _event):
        demo = Demo(user=self.user, text=self.tb.value)
        demo.save()
        self.demos.append(Li(str(demo)))

    def handle_request(self, request):
        self.user = request.user
        self.set_title("Lona Django Demo Project")
        self.demos = Ul()
        self.tb = TextInput(placeholder="Enter Text here")
        self.btn = Button("Save", handle_click=self.handle_btn)

        html = HTML(
            H1("Lona Django Demo Project"),
            self.demos,
            self.tb,
            self.btn,
        )

        for demo in Demo.objects.all():
            self.demos.append(Li(str(demo)))

        return html
