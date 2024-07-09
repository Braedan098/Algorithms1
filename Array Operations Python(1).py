
arr = [546.88,947.54,287.31,439.07,986.73,836.57,867.6,385.77,488.62,261.08,
404.21,36.39,376.45,55.97,382.69,203.55,449.56,115.08,108.5,211.57,956.53,879.09,
853.38,83.19,720.06,603.68,123.25,628.29,641.33,160.68,161.83,90.44,316.48,790.46,379.5,
867.97,424.83,986.89,831.9,995.13,450.68,647.08,516.39,568.63,231.54,502.61,220.15,783.17,76.05,64.62]
print("Initial array:", arr)


arr.insert(2, 10) 
print("Array after insertion:", arr)


arr[2] = 20  
print("Array after update:", arr)

arr.pop(2)  
print("Array after deletion:", arr)


search_element = 123.25
if search_element in arr:
    index = arr.index(search_element)
    print(f"Element {search_element} found at index:", index)
else:
    print(f"Element {search_element} not found in the array.")

def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                print(f"Step {i*n+j+1}: {arr}")
            if not swapped:
                break
print(arr)

def analyzeSortPerformance(data, description, time_complexity):
    print(f"\n{description} - Starting array: {data}")
    start = time.time()
    bubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) +
sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used:
{space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")

data_original = [546.88,947.54,287.31,439.07,986.73,836.57,867.6,385.77,488.62,261.08,404.21,36.39,376.45,55.97,382.69,203.55,449.56,115.08,108.5,211.57,956.53,879.09,853.38,83.19,720.06,603.68,123.25,628.29,641.33,160.68,161.83,90.44,316.48,790.46,379.5,867.97,424.83,986.89,831.9,995.13,450.68,647.08,516.39,568.63,231.54,502.61,220.15,783.17,76.05,64.62]

data_best = [36.39,55.97,64.62,76.05,83.19,90.44,108.5,115.08,123.25,160.68,161.83,203.55,211.57,220.15,231.54,261.08,287.31,316.48,376.45,379.5,382.69,385.77,404.21,424.83,439.07,449.56,450.68,488.62,502.61,516.39,546.88,568.63,603.68,628.29,641.33,647.08,720.06,783.17,790.46,831.9,836.57,853.38,867.6,867.97,879.09,947.54,956.53,986.73,986.89,995.13]

data_avg = [,947.54,287.31,439.07,986.73,836.57,603.68,261.08,404.21,36.39,55.97,382.69,203.55,449.56,115.08,108.5,211.57,64.62,956.53,879.09,83.19,720.06,450.68,995.13,123.25,546.88,628.29,641.33,160.68,161.83,90.44,316.48,790.46,379.5,867.97,424.83,488.62,986.89,385.77,853.38,647.08,516.39,568.63,231.54,376.45,502.61,220.15,867.6,783.17,76.05,831.9]

data_worst = [995.13,986.89,986.73,956.53,947.54,879.09,867.97,867.6,853.38,836.57,831.9,790.46,783.17,720.06,647.08,641.33,628.29,603.68,568.63,546.88,516.39,502.61,488.62,450.68,449.56,439.07,424.83,404.21,385.77,382.69,379.5,376.45,316.48,287.31,231.54,261.08,220.15,211.57,203.55,161.83,160.68,123.25,115.08,108.5,90.44,83.19,76.05,64.62,55.97,36.39]
analyzeSortPerformance(data_original, "Original Data", "O(n^2)")
analyzeSortPerformance(data_best, "Best Case (Sorted)", "O(n)")
analyzeSortPerformance(data_avg, "Average Case (Manually Shuffled)", "O(n^2)")
analyzeSortPerformance(data_worst, "Worst Case (Reverse Sorted)", "O(n^2)")
