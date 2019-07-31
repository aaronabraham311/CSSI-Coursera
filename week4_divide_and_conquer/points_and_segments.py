# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    # Labelling each point with either l, r, or p if it is respectively left end, right end or point
    starts = zip(starts, ['left'] * len(starts), range(len(starts)))
    ends = zip(ends, ['right'] * len(ends), range(len(ends)))
    points = zip(points, ['point'] * len(points), range(len(points)))

    # Sorting all points on number line
    sort_list = chain(starts, ends, points)
    sort_list = sorted(sort_list)

    segment_count = 0

    '''
    LOGIC:
    If you reach a left endpoint, you have started a new segment. Increment the segment counter
    If you reach a right endpoint, you have ended a segment, so decrement the segment counter
    If you reach a point, enter the number of segments you are currently in
    
    The index only matters for points.
    '''
    for num, label, index in sort_list:
        if label == 'left':
            segment_count += 1
        elif label == 'right':
            segment_count -= 1
        elif label == 'point':
            cnt[index] = segment_count
    return cnt

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
