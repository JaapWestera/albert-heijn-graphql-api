from __future__ import annotations

import logging

from typing import List, Optional

from dataclasses import dataclass
import requests
import aiohttp

from graphql.queries import BASKET_QUERY, PRODUCT_SEARCH
from .consts import API_ENDPOINT

_LOGGER = logging.getLogger(__name__)

AUTH_URL = "https://api.ah.nl/mobile-auth/v1/auth/token"
REFRESH_URL = "https://api.ah.nl/mobile-auth/v1/auth/token/refresh"


@dataclass
class AuthorizationResponse:
    accessToken: str
    refreshToken: str

    def __init__(
            self,
            accessToken: str,
            refreshToken: str
    ) -> None:
        """Initialize."""
        self.accessToken = accessToken
        self.refreshToken = refreshToken


@dataclass
class BasketItem:
    id: int
    quantity: int
    price: float
    brand: str
    title: str


class AlbertHeijn:
    accessToken: Optional[str]
    session: Optional[aiohttp.ClientSession] | requests.Session

    def __init__(self, session: Optional[aiohttp.ClientSession | requests.Session], accessToken: Optional[str] = None):
        self.accessToken = accessToken
        self.session = session or requests.Session()

    def getAuthenticatedHeaders(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % self.accessToken,
            "User-Agent": "Appie/8.22.3",
            "X-Application": "AHWEBSHOP"
        }

    async def authorize(self, token: str) -> AuthorizationResponse:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Appie/8.22.3",
            "X-Application": "AHWEBSHOP"
        }
        response = await self.session.request(
            "POST",
            AUTH_URL,
            headers=headers,
            data='{"clientId": "appie", "code": "%s"}' % token,
        )
        result = await response.json()
        print(result)
        self.accessToken = result['access_token']
        return AuthorizationResponse(result['access_token'], result['refresh_token'])

    async def refresh(self, refreshToken: str) -> AuthorizationResponse:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Appie/8.22.3",
            "X-Application": "AHWEBSHOP"
        }
        response = await self.session.request(
            "POST",
            REFRESH_URL,
            headers=headers,
            data='{"clientId": "appie", "refreshToken": "%s"}' % refreshToken,
        )
        result = await response.json()
        print('Refreshed authentication')
        print(result)
        self.accessToken = result['access_token']
        return AuthorizationResponse(result['access_token'], result['refresh_token'])

    async def getBasket(self) -> List[BasketItem]:
        response = await self.session.request(
            "POST",
            API_ENDPOINT,
            headers=self.getAuthenticatedHeaders(),
            json={"query": BASKET_QUERY}
        )
        json = await response.json()
        print(json)
        result = json['data']['basket']['products']
        print(result)
        basketItems = []
        for item in result:
            basketItems.append(
                BasketItem(id=item['id'], quantity=item['quantity'], price=item['product']['price']['now']['amount'],
                           brand=item['product']['brand'], title=item['product']['title']))
        print(basketItems)
        return basketItems

    async def productSearch(self, query: str):
        print(PRODUCT_SEARCH % query)
        response = await self.session.request(
            "POST",
            API_ENDPOINT,
            headers=self.getAuthenticatedHeaders(),
            json={"query": PRODUCT_SEARCH % query}
        )
        json = await response.json()
        print(json)
        result = json['data']['productSearch']
        print(result)
