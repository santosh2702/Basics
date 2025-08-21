def maxarea_bruteforce(height):
    max = 0
    for i in range(len(height)):
        for j in range(i + 1, n):
            area = min(height[i], height)
            if area > max:
                max = area
    return max
    

            
