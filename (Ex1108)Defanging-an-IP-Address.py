class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        add2 = address.split('.')
        return "[.]".join(add2)