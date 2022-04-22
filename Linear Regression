#get y value for given slope(m), y-intercept(b), 
#and x-value
def get_y(m, b, x):
  y = m*x + b
  return y
#test the function. Result should be 5.
#print(get_y(1, 2, 3))

#calculate the error or distance between a 
#line and a point
def calculate_error(m, b, point):
  x_point, y_point = point
  #point is a tuple
  return abs((get_y(m, b, x_point)) - y_point)

#test the function. y = 1x + 2
#the point (3, 7) is 2 units away from the line
#when we run the function, the result 
#should be 2
#print(calculate_error(1, 2, (3, 7)))


#calculate all error function
#adds errors for each point given a line
def calculate_all_error(m, b, datapoints):
  total_error = 0 #error start
  for point in datapoints: #pulls points from list
    point_error = calculate_error(m, b, point)
    total_error += point_error #sums all errors
  return total_error

datapoints = [(1, 3.5), (2, 5.8), (3, 6.4), (4, 9.8), (5, 10)]
#test the function for the points in the list. 
#all points in the list lie on the line y=x, 
#error should be 0
#print(calculate_all_error(1, 0, datapoints))

#calculate line of best fit through trial and error
#try different slopes and y intercepts to see which has smallest error
#define variable for possible slopes
possible_ms = [m*0.1 for m in range(-100, 100)]
#define variable for possible y-intercepts
possible_bs = [b*0.1 for b in range(-200, 200)]
smallest_error = float("inf") #starting value is large so the next error will be smaller
best_m = 0 #start
best_b = 0 #start
for m in possible_ms: #check slopes
  for b in possible_bs: #check y intercepts
    error = calculate_all_error(m, b, datapoints)
    if error < smallest_error:
        best_m = m
        best_b = b
        smallest_error = error
    #loops until the smallest error is found
print("y = " + str(best_m) + "x + (" + str(best_b) + "). Error: " + str(smallest_error))
