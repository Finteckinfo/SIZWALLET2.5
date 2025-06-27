from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from algosdk.account import generate_account
from algosdk import mnemonic
from dotenv import set_key

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

@api.get("/generate_wallet")
def generate_wallet(request):
    private_key, address = generate_account()
    mnem = mnemonic.from_private_key(private_key)
    set_key('.env', 'pk', private_key)
    set_key('.env', 'address', address)
    set_key('.env', 'mnemonic', mnem)
    return {
        "address": address,
        "private_key": private_key,
        "mnemonic": mnem
    }