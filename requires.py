from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class IperfRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:iperf}-relation-{joined,changed}')
    def changed(self):
        conv = self.conversation()
        if conv.get_remote('port'):
            conv.set_state('{relation_name}.available')

    @hook('{requires:iperf}-relation-{departed,broken}')
    def broken(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.available')
