###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Tavendo GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

try:
    import asyncio
except ImportError:
    # Trollius >= 0.3 was renamed
    import trollius as asyncio

from autobahn.asyncio.wamp import ApplicationSession


class Component(ApplicationSession):

    """
    An application component calling the different backend procedures.
    """

    @asyncio.coroutine
    def onJoin(self, details):

        yield from self.call('com.arguments.ping')
        print("Pinged!")

        res = yield from self.call('com.arguments.add2', 2, 3)
        print("Add2: {}".format(res))

        starred = yield from self.call('com.arguments.stars')
        print("Starred 1: {}".format(starred))

        starred = yield from self.call('com.arguments.stars', nick=u'Homer')
        print("Starred 2: {}".format(starred))

        starred = yield from self.call('com.arguments.stars', stars=5)
        print("Starred 3: {}".format(starred))

        starred = yield from self.call('com.arguments.stars', nick=u'Homer', stars=5)
        print("Starred 4: {}".format(starred))

        orders = yield from self.call('com.arguments.orders', u'coffee')
        print("Orders 1: {}".format(orders))

        orders = yield from self.call('com.arguments.orders', u'coffee', limit=10)
        print("Orders 2: {}".format(orders))

        arglengths = yield from self.call('com.arguments.arglen')
        print("Arglen 1: {}".format(arglengths))

        arglengths = yield from self.call('com.arguments.arglen', 1, 2, 3)
        print("Arglen 1: {}".format(arglengths))

        arglengths = yield from self.call('com.arguments.arglen', a=1, b=2, c=3)
        print("Arglen 2: {}".format(arglengths))

        arglengths = yield from self.call('com.arguments.arglen', 1, 2, 3, a=1, b=2, c=3)
        print("Arglen 3: {}".format(arglengths))

        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()
