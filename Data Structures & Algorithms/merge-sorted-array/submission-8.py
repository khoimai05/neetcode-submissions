class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
            return

        fi = 0
        boundary = m  # grows by 1 each time we place a nums2 element
        for num in nums2:
            while fi < boundary:
                if num >= nums1[fi]:
                    fi += 1
                else:
                    nums1[fi + 1:] = nums1[fi:-1]
                    nums1[fi] = num
                    boundary += 1
                    fi += 1
                    break
            else:
                # num is >= everything merged so far → place it right after
                nums1[fi] = num
                boundary += 1
                fi += 1