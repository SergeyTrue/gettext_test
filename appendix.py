
import gettext
import importlib

from gettext import gettext as _

importlib.reload(gettext)


def additional_print():
    print(_('three'))




