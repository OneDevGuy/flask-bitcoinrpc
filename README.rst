Flask-Wallet-RPC
================

.. module:: flask_wallet_rpc

Flask-Wallet-RPC is a Crypto Wallet RPC client extension for `Flask`_ , based on the
Python module `slick-bitcoinrpc`_.
Connects to the RPC server of your wallet.


Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Walet-RPC

or alternatively if you have pip installed::

    $ pip install Flask-Wallet-RPC


Configuration
-------------

To get started all you need to do is to instanciate a :class:`Walletrpc`
object after configuring the application::

    from flask import Flask
    from flask_wallet_rpc import Wallet, wallet

    app = Flask(__name__)
    app.config.from_pyfile('mysettings.cfg')
    w = Walletrpc(app)

    @app.route('/')
    def main():
        return wallet.getwalletinfo()

The `wallet` variable imported from :mod:`flask_wallet_rpc` always uses
the connection bound to the current Flask application context.

Walletrpc has one conf value required to connect to the wallets RPC Server
defaults:

`WALLET_RPC_URL`              The default URL, username and password to use
                              for communicating with the wallet daemon.

In your flask app config file add::

  WALLET_RPC_URL = "http://%s:%s@127.0.0.1:8332"%("Rpcuser", "Rpcpassword")

Replace Rpcuser and Rpcpassword with your wallets RPC info.


API
---

This part of the documentation documents each and every public class or
function from Flask-Coin.

Configuration
`````````````

.. autoclass:: Walletrpc
   :members:


.. _Flask: http://flask.pocoo.org/
.. _slick-bitcoinrpc: https://pypi.python.org/pypi/slick-bitcoinrpc
