from nameko.testing.services import worker_factory
from messenger.service import AyekooService

def test_ayekoo():
    # create worker from AyekooService class
    service = worker_factory(AyekooService)
    response = service.remark(name='a Test')
    assert response == 'This is a Test'