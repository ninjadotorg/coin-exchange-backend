from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from coin_exchange.business.crypto import AddressManagement
from coin_exchange.business.quote import QuoteManagement
from common.business import view_serializer_fields
from common.constants import CURRENCY


class AddressView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        currency = request.query_params.get('currency')
        if currency not in CURRENCY:
            raise ValidationError

        address, exists = AddressManagement.create_address(request.user.exchange_user, currency)
        return Response(address, status=status.HTTP_200_OK if exists else status.HTTP_201_CREATED)


class QuoteView(APIView):
    def get(self, request, format=None):
        serializer = QuoteManagement.get_quote(request.user, request.query_params)
        view_fields = ['amount', 'currency', 'fiat_currency', 'direction', 'fiat_local_currency',
                       'fiat_amount', 'fiat_local_amount',
                       'fiat_amount_cod', 'fiat_local_amount_cod']

        return Response(view_serializer_fields(view_fields, serializer.validated_data))


class QuoteReverseView(APIView):
    def get(self, request, format=None):
        serializer = QuoteManagement.get_quote_reverse(request.user, request.query_params)
        view_fields = ['amount', 'currency', 'fiat_currency', 'direction', 'fiat_local_currency',
                       'fiat_amount', 'fiat_local_amount',
                       ]

        return Response(view_serializer_fields(view_fields, serializer.validated_data))
