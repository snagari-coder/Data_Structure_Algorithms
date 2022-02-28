class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Counter is a special type of hash, which stores chars and freq in decending order
        count = collections.Counter(s)
        output = []
        #most_common(n) will return the top n most freq chars
        #most_common() returns all the chars with their frequencies in decending order
        for letter,freq in count.most_common():
            output.append(letter*freq)
        return ''.join(output)
            
# Basically we are building a hashmap, with chars and their corresponding frequencies
# Sorting the hashmap based on frequencies.
# Time = O(nlogn) for sorting
# Space = O(n) for hash.
