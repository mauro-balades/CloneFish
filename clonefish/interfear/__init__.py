
import asyncio
from clonefish.options import Options

from mitmproxy import options
from mitmproxy.tools import dump

class ProxyProvider:
    def __init__(self):
        pass

    def response(self, flow):
        print(f"New fetch! {flow.request.url}")


# TODO: inherit from a parent class called "Provider"
class InterfereProvider:
    options: Options

    def __init__(self, options: Options) -> None:
        self.options = options

    def execute(self):

        # TODO: https://github.com/mitmproxy/mitmproxy/discussions/5255#discussioncomment-2665643
        opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
        master = dump.DumpMaster(
            opts,
            with_termlog=False,
            with_dumper=False,
        )

        master.addons.add(ProxyProvider())
        # m.addons.add(core.Core())

        try:
            asyncio.run(master.run())
        except KeyboardInterrupt:
            master.shutdown()
