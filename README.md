# 2f-binning-III-resize-nonlinear-binsize-to-linear
resizes nonlinear binsizes to linear binsizes, by preserving the overall countnumbers in y, resampling, downsampling, 2D corresponding resorting of y-values

binsize = x(i+1)-x(i) // distance between to neighbored data points (x) // could be named sampling frequency
y(i) is then the corresponding value in y (correct: y(x))

Resampling - resizing binsizes means: 
x-axis has a ascending nonlinear scaling in the binsizes (non equidistant 
distances between neighboured datapoints, e.g. 1/x dependency, non constant sampling frequency, x(i+1)-x(i)>0 but NOT constant for all i) that should result in aequidistant (constant) binsizes. Compared to the biggest distance (maximum binsize) in the dataset, the smaller distances between all the other neighbored datapoints can be summarized, joined to a bigger binsize. That is called resampling, downsampling. Accordingly, the dependend y(x)-values have to be redistributet (e.g. summed). Usually the new binsize is not a integer multiple of the smaller binsizes, an overhang or rest results and hence, a redistribution (splitting) of (y(x)) to the according new binsize has to be implemented in order to preserve the overall value of the y-entries.

Note: this method linearizes nonlinear one axis of an 2D array, by downsampling it to a new samplingrate that has to be 1.5 times bigger than maximum binsize in the dataset. This method is NOT oversampling the dataset, it is NOT creating a smaller binsizes - something like this could be done using the 2f-binning II module which provides a linear interpolation for aequidistant datapoints. 


Example: 

original dataset:

x      y
1.3   1.0
1.4   100
1.5   234
1.6   110
...
2.5   3


the new binsize (sampling frequency) is e.g.:
binsize = 1.5
all other distances between neighboured datapoints are smaller, e.g. 1.3, 1.4, 1.5, 1.6.
To join these into a new binsize of 4 ((x*(j+1)-x*(j) =4): we summ x and y(x) until new binsize
is reached: x*(0)=1.3+1.4+1.5 = 4.2 and find 0.2 as an overhang (rest_x(0) in x*(0)).
Now, this overhang has to be distributet to the followed bin (new bins iterate with j, old ones with i).
and very important: the overhang ratio of the linked y*(x*(0)) is called rest_y has to be resorted to the y-value of the  x*(1)-bin, by substracting the corresponding amount from the previous y*(x*(0)).

i.a.w. 


for x*(j) <= binsize:

  x*(j) = rest_x(j-1)+sum(x(i))
  y*(j) = sum(y(i))

outer loop:
i+1
rest_x(j) = x*(j)-binsize
rest_y(j) = y*(j)(rest_x(j)/binsize)
j+1

For iteration j=0, x*(0)=4 with rest_x=0.2, the corresponding y*(0)=1+100+234-rest_y=335-rest_y, where rest_y=335*0.2/4=16.75 and this has to be added to the new y(j+1)* value. Note: this approach summarizes the rest_values in y relating to the whole new binsize. One could change this to a method, which weights a single overhang bin (e.g. y(i)=234 in our example above), in this case rest_y=y(i)*[(x(i)-x(i-1))/rest_x], 0.1/0.2

Note: python(x,y) 2.7x, numpy, tk dialog. saves .txt file
The programm asks for a two coloumn data set (.txt file, first coloumn x, second coloumn y, deciamal with ".", separation " ", sorted, first 3 rows are skipped). 
Needs cleaning and OOD, TDD
