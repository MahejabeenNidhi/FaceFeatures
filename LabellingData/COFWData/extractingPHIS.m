ds = load('COFW_test_color.mat');
phis = ds.phisT;
writematrix(phis, 'phisT.txt')