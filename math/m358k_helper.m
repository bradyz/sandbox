function m358k_helper(x, y)

% Least squares linear regression.
A = [ones(size(x, 2), 1), x'];
z = A \ y';

% Correlation.
c = corrcoef(x, y);

% Residuals.
r = A * z - y';
r2 = sum(r(:,1)' * r(:, 1));

% Plot.
b = z(1, 1);
a = z(2, 1);
xr = min(x):max(x);
keyboard;

fprintf('a: %f, b: %f, c: %f, r: %f\n', a, b, c(1, 2), r2);

plot(xr, xr*a + b, '-', x, y, '.', 'markersize', 25);
pause;
