import graphene
from graphene_django import DjangoObjectType
from .models import Payment, PaymentDetail
from core import prefix_filterset, filter_validity, ExtendedConnection


from contribution.schema import PremiumGQLType


class PaymentGQLType(DjangoObjectType):
    class Meta:
        model = Payment
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "uuid": ["exact"],
            "status": ["exact"],
            "expected_amount": ["exact", "lt", "lte", "gt", "gte"],
            "received_amount": ["exact", "lt", "lte", "gt", "gte"],
            "transfer_fee": ["exact", "lt", "lte", "gt", "gte"],
            "officer_code": ["exact"],
            "phone_number": ["exact", "istartswith", "icontains", "iexact"],
            "request_date": ["exact", "lt", "lte", "gt", "gte"],
            "received_date": ["exact", "lt", "lte", "gt", "gte"],
            "matched_date": ["exact", "lt", "lte", "gt", "gte"],
            "payment_date": ["exact", "lt", "lte", "gt", "gte"],
            "date_last_sms": ["exact", "lt", "lte", "gt", "gte"],
            "transaction_no": ["exact", "istartswith", "icontains", "iexact"],
            "origin": ["exact", "istartswith", "icontains", "iexact"],
            "receipt_no": ["exact", "istartswith", "icontains", "iexact"],
            "rejected_reason": ["exact", "istartswith", "icontains", "iexact"],
            "language_name": ["exact", "istartswith", "icontains", "iexact"],
            "type_of_payment": ["exact", "istartswith", "icontains", "iexact"]
        }
        connection_class = ExtendedConnection


class PaymentDetailGQLType(DjangoObjectType):
    class Meta:
        model = PaymentDetail
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "product_code": ["exact"],
            "insurance_number": ["exact"],
            "policy_stage": ["exact"],
            "expected_amount": ["exact", "lt", "lte", "gt", "gte"],
            "amount": ["exact", "lt", "lte", "gt", "gte"],
            "enrollment_date": ["exact", "lt", "lte", "gt", "gte"],
            **prefix_filterset("premium__", PremiumGQLType._meta.filter_fields),
            **prefix_filterset("payment__", PaymentGQLType._meta.filter_fields)
        }
        connection_class = ExtendedConnection
