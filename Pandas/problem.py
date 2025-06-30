def bubble_sort(scores):
    n = len(scores)  
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
    return scores
n = 5
scores = [55, 90, 70, 60, 80]
sorted_scores = bubble_sort(scores)
print("Sorted scores:", sorted_scores)