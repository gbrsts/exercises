# The task is simple. Through some critical points in 2D, you have to draw a wave like curve. 
# Your goal is to include as many points as possible.

# There will be an imaginary line y = a, which we call the major axis for the curve.
# All the points on the curve should have different x coordinates. Their y coordinates should be of form a-1 or a+1.

# Two consecutive points on the curve should have a difference of 2 in their y coordinate.

# Input
# There will be no more than 222 test cases. Each test case starts with an integer N, 
# the number of points in the test case. In the next N lines, there will be N pair of integers giving the x and y coordinate of the points. 
# There will be no more than 1000 points in each test case. All coordinates are integers -- they'd fit in a signed 2 byte integer data type. 
# The data must be read of default input.

# Output
# For each test case print a number -- the maximum number of critical points that can be included in a curve drawn from the given points.

