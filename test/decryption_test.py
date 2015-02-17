#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('..')

from encryption import decrypt


def setup():
    global cleartext, offset
    cleartext = 'the quick brown fox jumps over the lazy dog'
    offset = 3


@with_setup(setup())
def test_decrypt_takes_a_string_and_offset_as_arguments():
    assert_raises(TypeError, decrypt)
    assert_raises(TypeError, decrypt, cleartext)

# Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C eller A-nivå
def test_decrypt_raises_ValueError_if_called_with_empty_string():
    with assert_raises(ValueError) as e:
        decrypt('', offset)
    assert_equal(e.exception.message, 'can not decrypt empty string')


# Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C eller A-nivå
def test_decrypt_raises_ValueError_if_called_with_zero_offset():
    with assert_raises(ValueError) as e:
        decrypt(cleartext, 0)
    assert_equal(e.exception.message, 'offset must not be zero')


def test_decrypt_returns_a_string():
    assert_is_instance(decrypt(cleartext, offset), str)


def test_decrypt_returns_the_decrypted_string():
    assert_equal(decrypt('WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ', 3),  cleartext)
    assert_equal(decrypt('GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT', 13), cleartext)
    assert_equal(decrypt('YMJ VZNHP GWTBS KTC OZRUX TAJW YMJ QFED ITL', 5),  cleartext)


def test_decrypt_works_with_negative_offsets():
    assert_equal(decrypt('RFC OSGAI ZPMUL DMV HSKNQ MTCP RFC JYXW BME', -2),  cleartext)
    assert_equal(decrypt('IWT FJXRZ QGDLC UDM YJBEH DKTG IWT APON SDV', -11), cleartext)
    assert_equal(decrypt('PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC', -4),  cleartext)


