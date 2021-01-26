import gettext
ru = gettext.translation('base', localedir=r'C:\Users\belose\PycharmProjects\test_gettext\locales', languages=['ru'])
ru.install()
_ = ru.gettext
# _ =gettext.gettext

class Output:

    def additional_print(self):
        print(_('three'))




