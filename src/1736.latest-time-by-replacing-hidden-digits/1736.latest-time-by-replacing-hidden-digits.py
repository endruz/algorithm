class Solution1:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == "?":
            if time[1] == "?":
                time[0] = "2"
                time[1] = "3"
            elif "0" <= time[1] <= "3":
                time[0] = "2"
            else:
                time[0] = "1"
        if time[1] == "?":
            if time[0] == "2":
                time[1] = "3"
            else:
                time[1] = "9"
        if time[3] == "?":
            time[3] = "5"
        if time[4] == "?":
            time[4] = "9"
        return "".join(time)


class Solution2:
    """
    Solution1 优化
    """
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == "?":
            time[0] = "2" if time[1] in ("0", "1", "2", "3", "?") else "1"
        if time[1] == "?":
            time[1] = "3" if time[0] == "2" else "9"
        if time[3] == "?":
            time[3] = "5"
        if time[4] == "?":
            time[4] = "9"
        return "".join(time)
