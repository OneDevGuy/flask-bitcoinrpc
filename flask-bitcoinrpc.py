from __future__ import absolute_import
from flask import current_app, _app_ctx_stack
from slickrpc import Proxy


class Bitcoinrpc(object):
    """Central controller class that can be used to configure how
    Flask-Coin behaves.  Each application that wants to use Flask-Coin
    has to create, or run :meth:`init_app` on, an instance of this class
    after the configuration was initialized.
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BITCOIN_RPC_URL', '"http://%s:%s@127.0.0.1:8332"%("StakerUI", "1triclypassword!")')
        app.teardown_appcontext(self.teardown)
        # with open('BITCOIN_RPC_URL', 'r') as rpcdata:
        #     rpcauth=rpcdata.read()
        #
        # bitcoin = Proxy("http://{0:1}@127.0.0.1:8332".format(BITCOIN_RPC_URL))


    def connect(self):
        return Proxy(current_app.config['BITCOIN_RPC_URL'])


    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'bitcoin_rpc'):
            ctx.bitcoin_rpc.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'bitcoin_rpc'):
                ctx.bitcoin_rpc = self.connect()
        return ctx.bitcoin_rpc

# rpc.init_app(app)
#
# wallet_info = rpc.connection.getinfo()
