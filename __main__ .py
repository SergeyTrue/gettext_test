import gettext
from appendix import Output
from pathlib import Path
LOCALEDIR = Path(__file__).parent / 'locales'
def print_some_strings():
    print(_("one"))
    print(_("two"))


def reload_lang(lang):
    import gettext
    ru = gettext.translation('base', localedir=LOCALEDIR, languages=['ru'])
    ru.install()

    global _
    if lang == 'RUSSIAN':
        _ = ru.gettext
    elif lang == 'ENGLISH':
        _ =gettext.gettext
    return _



lang = 'ENGLISH'
_ = reload_lang(lang)

print_some_strings()
a = Output()
a.lang = _
a.additional_print()

