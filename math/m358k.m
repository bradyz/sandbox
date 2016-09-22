x = [6.6, 8.3, 6.2, 6.6, 6.9, 7.4];
y = [60, 503, 115, 65, 62, 1];

A = [ones(size(x))', x'];
b = y';
c = A\b
xr = min(x):max(x)

plot(xr, xr*c(2, 1) + c(1, 1), '-', x, y, '.', 'markersize', 20);
pause;

corrcoef(x, y)

x = [6.6, 6.2, 6.6, 6.9, 7.4];
y = [60, 115, 65, 62, 1];

A = [ones(size(x))', x'];
b = y';
c = A\b
xr = min(x):max(x)

plot(xr, xr*c(2, 1) + c(1, 1), '-', x, y, '.', 'markersize', 20);
pause;
