class LineSweep :
    def findIfOverlap(self, intervals):
        points = []

        for interval in intervals :
            points.append(interval[0],-1)
            points.append(interval[0], 1)

        points.sort()
        count = 0
        for point in points :
            if point[1] == -1 :
                count += 1
            else :
                count -= 1

            if count > 0 :
                return True

        return False

    def mergeIntervals(self, intervals):

        points = []

        for interval in intervals :
            points.append(interval[0],-1)
            points.append(interval[0], 1)

        points.sort()
        result = []
        count = 0
        for point in points :
            if point[1] == -1 :
                count += 1
                if count == 1 :
                    result.append([point[0],None])
            else :
                count -= 1

            if count == 0 :
                result[-1][1] = point[0]

        return result


    def merge(self, intervals):
        result = []
        intervals.sort()
        for interval in intervals :
            if len(result) > 0 and result[-1][1] >= interval[0] :
                result[-1][1] = max(result[-1][1],interval[1])
            else :
                result.append(interval)

        return result

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        map = {}
        points = []

        for building in buildings:
            points.append([building[0], -1, building[2]])
            points.append([building[1], 1, building[2]])
        points.sort()

        # print(points)
        result = []
        currentMax = 0
        count = 0
        for point in points:
            if point[1] == -1:
                map[point[2]] = map.get(point[2], 0) + 1
                if currentMax < point[2]:
                    if len(result) == 0 or point[0] > result[-1][0]:
                        result.append([point[0], point[2]])
                    else:
                        result[-1][1] = point[2]
                    currentMax = point[2]

                count += 1
            else:
                map[point[2]] -= 1
                count -= 1
                if map[point[2]] == 0:
                    del map[point[2]]
                # print(map)
                if count == 0:
                    currentMax = 0
                    result.append([point[0], 0])
                else:
                    if currentMax == point[2] and point[2] not in map:
                        currentMax = max(map.keys())
                        result.append([point[0], currentMax])

        return result

