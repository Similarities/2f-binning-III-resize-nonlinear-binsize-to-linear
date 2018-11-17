# 2f-binning-III-resize-nonlinear-binsize-to-linear
resizes nonlinear binsizes to linear binsizes, by preserving the overall countnumbers in y, oversampling, resorting of y-values


The programm asks for a two coloumn data set (.txt file, first coloumn x, second coloumn y, deciamal with ".", separation " ", sorted, first 3 rows are skipped). Here, resizing binsizes means: x-axis has a ascending nonlinear scaling in the binsizes (non equidistant 
distances between neighboured datapoints, e.g. 1/x dependency) that should result in aequidistant (constant) binsizes. According the biggest distance that exists between to datapoints in the dataset, the smaller distance between all the other datapoints can be summarized, joined to this bigger binsize. That is called resizing. Accordingly the y-values have to be redistributet (e.g. summed). As often the new binsize is not a integer multiple of the smaller binsizes, here a redistribution (splitting) has to be implemented. 

Example: 
the resulting (by this maximum binsize) is 4, all other distances between neighboured datapoints are smaller, e.g. 1.3, 1.4, 1.5, 1.6 - To join these into a new binsize of 4 (iteration i=0): we summ (x and y) until new binsize (4, i=0) is reached: 1.3+1.4+1.5 = 4.2 and find 0.2 as an overhang (rest) in x and y. This overhang has to be distributet now to the followed bin (i=1) and very important: the ratio of the linked y-value has to be resorted to the y-value of the new (i=1) bin by substracting it from the previous bin (i=0).
For interation i=0, the y(i)*=(y(1.3)+ y(1.4)+ y(1.5)) - y(i)= 0.2*(y(i)*-1), for iteration i=1 : y(i)*0.2 has to be added to the new y(i+1)* value. Same counts for the next x bin

Note: python(x,y) 2.7x, numpy, tk dialog. saves .txt file
Needs cleaning and OOD, TDD
