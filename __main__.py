import gettext
from appendix import Output


def print_some_strings():
    print(_("one"))
    print(_("two"))


ru = gettext.translation('base', localedir=r'C:\Users\belose\PycharmProjects\test_gettext\locales', languages=['ru'])
ru.install()
_ = ru.gettext
# _ = gettext.gettext


print_some_strings()
a = Output()
a.additional_print()
