from nameko.rpc import rpc

class AyekooService:

    name = 'ayekoo'

    @rpc
    def remark(self, name):
        return f'This is {name}'