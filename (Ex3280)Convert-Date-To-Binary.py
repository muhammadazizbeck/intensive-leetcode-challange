class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        next_date = date.split("-")
        bin_date = [bin(int(nextr))[2:] for nextr in next_date]
        return "-".join(bin_date)
        