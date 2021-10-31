from django.apps import apps
from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.permissions import AllowAny

from common.permissions import IsAdmin, IsOwner, IsStaff

from ..models import Accounts, Employees, DriverWallets
from .serializers import (
    CashNdsSerializer,
    EmployeesRetriveSerializer,
    EmployeesStaffSerializer,
    EmployeesUpdateSerializer,
    PaylipsSerializer,
    PerformancesSerializer,
    TimesheetsSerializer, DriverWalletsSerializer,
)

User = get_user_model()


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def get_queryset(self):
        user = self.request.user
        if user.type.lower() == "staff":
            return Employees.objects.filter(country=user.country)
        return Employees.objects.all()

    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [IsAdmin | IsStaff | IsOwner]
        else:
            permission_classes = [IsAdmin | IsStaff]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.type.lower() == "employee":
            if self.action == "retrieve":
                return EmployeesRetriveSerializer
            elif self.action == "update":
                return EmployeesUpdateSerializer
        return EmployeesStaffSerializer

    def perform_create(self, serializer):
        employee = serializer.save()

        payroll_account = Accounts.objects.create(
            name=employee.name, account_category_id=2, account_type_id=2, employee_id=employee.id
        )
        payroll_account.save()

        salary_account = Accounts.objects.create(
            name=employee.name, account_category_id=4, account_type_id=9, employee_id=employee.id
        )
        salary_account.save()


class GeneralList(generics.ListAPIView):
    lookup_field = "employee"
    lookup_url_kwarg = "employee_id"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_name = None

    def dispatch(self, request, *args, **kwargs):
        model_name = self.kwargs.get("model_name").lower()

        if (
            model_name == "timesheets"
            or model_name == "performances"
            or model_name == "cashnds"
            or model_name == "payslips"
        ):
            self.model_name = model_name
            return super().dispatch(request, *args, **kwargs)

        raise Http404

    def get_permissions(self):
        if self.kwargs.get("employee_id"):
            permission_classes = [IsAdmin | IsStaff | IsOwner]
        else:
            permission_classes = [IsAdmin | IsStaff]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        try:
            model = apps.get_model(app_label="employees", model_name=self.model_name)

            user = self.request.user
            employee_id = self.kwargs.get("employee_id")
            month = self.kwargs.get("month")
            year = self.kwargs.get("year")
            day = self.kwargs.get("day")

            employee_objects = model.objects.all()

            if employee_id:
                employee_objects = employee_objects.filter(employee=employee_id)

            if month and year:
                employee_objects = employee_objects.filter(date_selected__year=year, date_selected__month=month)

            if day and month and year:
                employee_objects = employee_objects.filter(date_selected__year=year, date_selected__month=month,
                                                           date_selected__day=day)

            if user.type.lower() == "staff":
                employee_objects = employee_objects.filter(country=user.country)

            return employee_objects
        except LookupError:
            raise Http404

    def get_serializer_class(self):
        if self.model_name == "timesheets":
            return TimesheetsSerializer
        elif self.model_name == "performances":
            return PerformancesSerializer
        elif self.model_name == "payslips":
            return PaylipsSerializer
        elif self.model_name == "cashnds":
            return CashNdsSerializer
        raise Http404


class DepositSlipAPIView(CreateAPIView):
    serializer_class = DriverWalletsSerializer


class CashNdsAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        emp_id = kwargs.get('employee_id', None)
        outgoing_trans_amount = DriverWallets.objects.filter(employee=emp_id, trans_type="outgoing").\
            aggregate(outgoing = Sum('trans_amount'))
        incoming_trans_amount = DriverWallets.objects.filter(employee=emp_id, trans_type="incoming").\
            aggregate(incoming = Sum('trans_amount'))
        if incoming_trans_amount["incoming"] is None:
            incoming_trans_amount["incoming"] = 0
        if outgoing_trans_amount["outgoing"] is None:
            outgoing_trans_amount["outgoing"] = 0
        cash_n_ds = outgoing_trans_amount["outgoing"] - incoming_trans_amount["incoming"]
        return Response({"cash_n_ds": cash_n_ds})

