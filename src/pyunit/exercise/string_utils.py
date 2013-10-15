# coding: utf-8

class StringUtils(object):
    @classmethod
    def toSnakeCase(cls, string):
        ret = ''
        for i in range(len(string)):
            c = string[i]
            if c == c.upper():
                if i == 0:
                    c = c.lower()
                else:
                    c = '_' + c.lower()
            ret += c
        return ret


