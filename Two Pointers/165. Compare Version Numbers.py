# https://leetcode.com/problems/compare-version-numbers/?envType=daily-question&envId=2024-05-03

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")

        i = 0
        j = 0

        while i < len(version1) and j < len(version2):
            if int(version1[i]) > int(version2[j]):
                return 1
            elif int(version1[i]) < int(version2[j]):
                return -1
            
            i += 1
            j += 1
        
        while i < len(version1):
            if int(version1[i]) != 0:
                return 1
            
            i += 1
        
        while j < len(version2):
            if int(version2[j]) != 0:
                return -1
            
            j += 1
        
        return 0
                
    # optimizing is to not create lists and instead iterate using two pointers and keep track of "."