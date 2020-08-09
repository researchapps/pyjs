#
# This is taken from the python module gettext
# Some things won't work (ugettext/ungettext/install)
# These might work in a subclass of NullTranslations

class NullTranslations:
    def __init__(self, fp=None):
        self._info = {}
        self._charset = None
        self._output_charset = None
        self._fallback = None
        if fp is not None:
            self._parse(fp)

    def _parse(self, fp):
        pass

    def add_fallback(self, fallback):
        if self._fallback:
            self._fallback.add_fallback(fallback)
        else:
            self._fallback = fallback

    def gettext(self, message):
        if self._fallback:
            return self._fallback.gettext(message)
        return message

    def lgettext(self, message):
        if self._fallback:
            return self._fallback.lgettext(message)
        return message

    def ngettext(self, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.ngettext(msgid1, msgid2, n)
        if n == 1:
            return msgid1
        else:
            return msgid2

    def lngettext(self, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.lngettext(msgid1, msgid2, n)
        if n == 1:
            return msgid1
        else:
            return msgid2

    def ugettext(self, message):
        if self._fallback:
            return self._fallback.ugettext(message)
        return str(message)

    def ungettext(self, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.ungettext(msgid1, msgid2, n)
        if n == 1:
            return str(msgid1)
        else:
            return str(msgid2)

    def info(self):
        return self._info

    def charset(self):
        return self._charset

    def output_charset(self):
        return self._output_charset

    def set_output_charset(self, charset):
        self._output_charset = charset

    def install(self, str=False, names=None):
        import builtins
        builtins.__dict__['_'] = str and self.ugettext or self.gettext
        if hasattr(names, "__contains__"):
            if "gettext" in names:
                builtins.__dict__['gettext'] = builtins.__dict__['_']
            if "ngettext" in names:
                builtins.__dict__['ngettext'] = (str and self.ungettext
                                                             or self.ngettext)
            if "lgettext" in names:
                builtins.__dict__['lgettext'] = self.lgettext
            if "lngettext" in names:
                builtins.__dict__['lngettext'] = self.lngettext

