from dj_rest_auth.views import (
    LoginView
)
from rest_framework import status
from rest_framework.response import Response

from employees.models import Employees


class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        if self.user.type != "employee":
            content = {"Error message": "User must be an employee."}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        mydata = {"employee_id": Employees.objects.get(user_id=self.user).id}
        orginal_response.data.update(mydata)
        return orginal_response
