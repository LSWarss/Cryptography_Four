from encryptions.symetric import Symmetric

test_key = "ZroWmwN2IZSbIcRN7pjwNeZsVD1wVdCFhUYNpVyGQ9k="
test_string = "Test input message"
test_encrypted_string = "gAAAAABgaxSuLpu05Uy8rrWMh5OfKnWoZGlUIABBQmqzzkoW939pj6qpSClud_m2MtYJDggLKXD4-hP9XdLNw4EC6YvmEkQo_KqDVk7ZYvgFinzJaOwsegA="
symmetric_instance = Symmetric(test_key)

def test_initialization():
    assert symmetric_instance.key != None
    assert symmetric_instance.fernet != None

def test_keyGen() :
    assert symmetric_instance.generate_key() != None

def test_encryption():
    assert type(symmetric_instance.encode(test_string)) == bytes

def test_decryption():
    assert type(symmetric_instance.decode(test_encrypted_string)) == bytes