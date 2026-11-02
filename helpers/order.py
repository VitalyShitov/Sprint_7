import requests

from urls import (
    ORDER_CREATE_URL,
    ORDERS_LIST_URL,
    ORDER_BY_TRACK_URL,
    ORDER_CANCEL_URL,
)


def create_order(payload):
    return requests.post(ORDER_CREATE_URL, json=payload)


def get_orders_list():
    return requests.get(ORDERS_LIST_URL)


def get_order_by_track(track):
    params = {"t": track}
    return requests.get(ORDER_BY_TRACK_URL, params=params)


def cancel_order(track):
    payload = {"track": track}
    return requests.put(ORDER_CANCEL_URL, json=payload)
