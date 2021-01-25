import gettext
from appendix import additional_print




en = gettext.translation('base', localedir=r'C:\Users\belose\PycharmProjects\test_gettext\locales', languages=['en'])
en.install()
_ = en.gettext



def print_some_strings():
    print(_("one"))
    print(_("two"))


if __name__ == '__main__':

    print_some_strings()
    additional_print()
