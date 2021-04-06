from encryptions.asymetric import Assymetric

test_string = "It's a trap!"
test_encrypted_string = "13303aa602e4bf9b9e5d813954baf9e62a776a7dba4135a1f7c3c3430ba6e8437126f360889f5e12143b921c2c977511469ff6d1f8241e48bee2c1877c93e12e530ecf53ca91b916805344a0fbec4e1fc7f0741049cc3cb336e74b0b372b1d424f0f8f342f7ca2d487b26d3baff44b7fcf46ea7ef5222987f665d7fa6545422ce84f2c594103edf1a60d3de9def00502869de9df272e986c636bae40a6df406ad1576f3d70d0b935ec4e0583492e4f0cbd06d0ac7062c995250cec0e9735e33a0b16cbfaf65615787dff66295d8c194345e01f89cd43bdca16b320b4d0e6c23d0ce49febde7449654da9bc6bd9548bbadf22f7b89127f4532304cf3f71ae5800"
assymetric_instance = Assymetric()

def test_initialization():
    assert assymetric_instance.get_keys()[0] == None
    assert assymetric_instance.get_keys()[1] == None
    assymetric_instance.generate_keys()
    assert assymetric_instance.get_keys()[0] != None
    assert assymetric_instance.get_keys()[1] != None

def test_keysGen():
    assert assymetric_instance.generate_keys() != None

def test_keysGenSSH():
    assert Assymetric.generate_ssh_keys() != None

def test_enrypt():
    assert assymetric_instance.encrypt(test_string) != None
    assert type(assymetric_instance.encrypt(test_string)) == str

def test_decrypt():
    assert assymetric_instance.decrypt(test_encrypted_string) != None
    assert type(assymetric_instance.decrypt(test_encrypted_string)) == str