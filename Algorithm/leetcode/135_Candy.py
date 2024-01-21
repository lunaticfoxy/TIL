class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        We have to find "Peak" and "Valley"
        Valley is more important beacuase candy number for each child
        is ininitalized to 1 in each Valley
        And we can find max candy number for each child using Peak

        We will divide ratings in sections that between Valleies,
        And divide section to increasing section and decreasing section again.

        We can easliy calculate candies in increasing section and decreasing section.
        Then all number of candy will be found

        Time Complexity: O(n) - It iterate ratings once
        Space Complexity: O(1) - It uses only extra several variables, no iteratable objects
        """
        all_candy = 0

        # interate all ratings
        i = 0
        while i < len(ratings):
            cur_candy = 0
            inc_cnt = 0
            desc_cnt = 0
            # find peak
            while i < len(ratings)-1 and ratings[i+1] > ratings[i]:
                inc_cnt += 1
                i += 1
            
            # find valley after peak
            while i < len(ratings)-1 and ratings[i+1] < ratings[i]:
                desc_cnt += 1
                i += 1
            
            # Candy num in current section can be calcuated sum of these
            # - candies in peak: max(increasing size, decresing size) + 1
            # - candies in increasing section: sum of arithmetic sequence 1 to inc_cnt
            # - candies in decresing section:  sum of arithmetic sequence 1 to desc_cnt
            cur_candy = max(inc_cnt, desc_cnt)+1
            cur_candy += inc_cnt*(inc_cnt+1)/2
            cur_candy += desc_cnt*(desc_cnt+1)/2
            all_candy += int(cur_candy)

            # if there is no decresing section (= same rating found)
            # we can initialize candy numer like Valley
            # Then increase index and start next section in there
            if desc_cnt==0:
                i += 1
            else:
                # If there is decressing section
                # We will start next section from bottom of valley
                # But cur_candy already contains candies in bottom
                # Then, we remove candies in bottom (in fact, a candy) from all_candy
                all_candy -= 1

        return all_candy
