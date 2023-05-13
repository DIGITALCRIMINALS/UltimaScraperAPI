from datetime import datetime
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import ultima_scraper_api

    auth_types = ultima_scraper_api.auth_types
    user_types = ultima_scraper_api.user_types


class SubscriptionModel:
    def __init__(
        self, data: dict[str, Any], user: "user_types", subscriber: "auth_types"
    ) -> None:
        self.id = user.id
        self.username = user.username
        self.name = user.name
        self.active = data["subscribedBy"]
        self.subscribed_by_data: dict[str, Any] = data["subscribedByData"]
        self.subscribed_by_expire: bool = data["subscribedByExpire"]
        self.subscribed_by_expire_date: datetime = datetime.fromisoformat(
            data["subscribedByExpireDate"]
        )
        self.subscribed_by_autoprolong: bool = data["subscribedByAutoprolong"]
        self.subscribed_is_expired_now: bool = data["subscribedIsExpiredNow"]
        self.current_subscribe_price: int = data["currentSubscribePrice"]
        self.subscribed_on: bool = data["subscribedOn"]
        self.subscribed_on_data: dict[str, Any] = data["subscribedOnData"]
        self.subscribed_on_expired_now: bool = data["subscribedOnExpiredNow"]
        self.subscribed_on_duration: str = data["subscribedOnDuration"]
        self.subscribe_price: int = data["subscribePrice"]
        self.user = user
        self.subscriber = subscriber
        self.__raw__ = data

    def is_active(self):
        return bool(self.active)

    def get_api(self):
        return self.subscriber.get_api()

    def get_authed(self):
        return self.subscriber.get_authed()