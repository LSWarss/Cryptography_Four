from encryptions.asymetric import Assymetric

assymetric_instance = Assymetric("test", "test")

def test_initialization():
    assert assymetric_instance.private_key != None
    assert assymetric_instance.public_key != None

def test_keysGen():
    assert Assymetric.generate_keys() != None

def test_keysGenSSH():
    assert Assymetric.generate_ssh_keys() != None

