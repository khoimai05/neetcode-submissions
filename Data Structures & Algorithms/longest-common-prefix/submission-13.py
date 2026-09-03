class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for w in strs:
            if w.startswith(prefix):
                continue
            else:
                print('-------')
                if len(w) == 0:
                    return ""
                miner = min(len(w),len(prefix))
                for i in range(miner):
                    print(f"{prefix}| {w}| {i}")
                    if w[i] == prefix[i]:
                        if i == miner -1:
                            prefix = w[0:i+1]
                        continue
                    else:
                        if i == 0:
                            return ""
                        prefix = w[0:i]
                        break
        return prefix
        