# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from decimal import Decimal

from rest_framework.response import Response
from rest_framework.views import APIView

from coin_exchange.constants import CONFIG_USER_LIMIT
from coin_system.models import Config
from common.business import PriceManagement, RateManagement
from common.constants import SUPPORT_CURRENCIES, LANGUAGE, CURRENCY
from integration import coincap
from notification.business import ComparePriceNotification
from integration.bitstamp import get_price


class CurrencyRateView(APIView):
    def post(self, request, format=None):
        RateManagement.save_rates()

        return Response(True)


class CryptoRateView(APIView):
    def get(self, request, format=None):
        result = []
        for currency in SUPPORT_CURRENCIES:
            price = PriceManagement.get_cache_price(currency)
            result.append({
                'buy': price.buy,
                'sell': price.sell,
                'currency': currency,
            })
        return Response(result)

    def post(self, request, format=None):
        for currency in SUPPORT_CURRENCIES:
            PriceManagement.save_cache_price(currency)

        return Response(True)


class CurrencyLevelLimitView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request, format=None):
        currency = request.query_params.get('currency', '')
        keys = Config.objects.filter(key__istartswith=currency).order_by('key')
        splitter = CONFIG_USER_LIMIT.format('', '')
        limits = list(map(lambda key: {
            'currency': key.key.split(splitter)[0],
            'level': key.key.split(splitter)[1],
            'limit': key.value,
        }, keys))

        return Response(limits)


class LanguageView(APIView):
    def get(self, request, format=None):
        return Response({
            LANGUAGE.en: LANGUAGE[LANGUAGE.en],
            LANGUAGE.hk: LANGUAGE[LANGUAGE.hk],
        })


class ComparePrice(APIView):
    def get(self, request, format=None):
        result = []
        coins = [
            (CURRENCY.BTC, 'bitcoin'),
            (CURRENCY.ETH, 'ethereum')
        ]
        for currency in coins:
            price = coincap.get_rate(currency[1])
            if Decimal(get_price(currency[0])) >= price['rateUsd']:
                ComparePriceNotification.send_new_compare_price_notification(price)
                result.append(price)

        return Response(result)
