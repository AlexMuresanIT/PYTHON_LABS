import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
from matplotlib import pylab as pl
import logging
import datetime
import collections
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

#Creare clasa client
class Client:
    def __int__(self):
        random=Crypto.Random.new().read
        self.private_key=RSA.generate(1024,random)
        self.public_key=self.private_key.public_key()
        self.signer=PKCS1_v1_5.new(self.private_key)

    @property
    def identity(self):
        return binascii.hexlify(self.public_key.export_key(format="DER")).decode("ascii")

class Transaction:
    def __init__(self,sender,recipient,value):
        self.sender=sender
        self.recipient=recipient
        self.value=value
        self.time=datetime.datetime.now()

    def to_dict(self):
        if self.sender=="Genesis":
            identity="Genesis"
        else:
            identity=self.sender.identity
        return collections.OrderedDict({"sender":identity,
                                        "recipient":self.recipient,
                                        "value":self.value,
                                        "time":self.time})

    def sign_trans(self):
        private_key=self.sender
        signer=PKCS1_v1_5.new(private_key)
        h=SHA.new(str(self.to_dict()).encode("utf-8"))
        return binascii.hexlify(signer.sign(h)).decode("ascii")

p1=Client
p2=Client

t=Transaction(p1,p2.identity,5000)
private_key_sender=t.sign_trans()
print(private_key_sender)