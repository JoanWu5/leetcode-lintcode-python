from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words or maxWidth == 0:
            return []
        
        result = []
        
        line = []
        count = 0
        
        for word in words:
            if count + len(word) + len(line)<= maxWidth:
                line.append(word)
                count += len(word)
            else:
                string = ""
                if len(line) == 1:
                    string = line[0] + " " * (maxWidth - count)
                else:
                    space = (maxWidth - count) // (len(line) - 1)
                    left = (maxWidth - count) % (len(line) - 1)

                    for i in range(len(line) - 1):
                        string += line[i]
                        string += " " * space
                        if left != 0:
                            string += " " 
                            left -= 1
                    string += line[-1]
                result.append(string)
                line = [word]
                count = len(word)
        
        string = ""
        if len(line) == 1:
            string = line[0] + " " * (maxWidth - count)
        else:
            count = 0
            for i in range(len(line) - 1):
                string += line[i]
                string += " "
                count += len(line[i]) + 1
            string += line[-1]
            count += len(line[-1])
            string += " " * (maxWidth - count)
        result.append(string)
        return result
                