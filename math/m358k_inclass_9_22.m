distance = [36 67 93 142 474 776 1784 2796 3707];
length = [0.24 0.61 1.00 1.88 11.86 29.46 84.07 164.82 247.68];

A = [ones(size(distance, 2), 1), distance'];
x = A \ length';

% Residuals.
r = A * x - length';
r2 = sum(r(:,1)' * r(:, 1))
corrcoef(distance, length)

% Plot.
b = x(1, 1);
a = x(2, 1);
xr = min(distance):max(distance);

plot(xr, xr*a + b, '-', distance, length, '.', 'markersize', 25);
pause;

% Normalize with log.
y = log(length);
x = A \ y';

% Residuals.
corrcoef(distance, y)

% Plot.
b = x(1, 1);
a = x(2, 1);
xr = min(distance):max(distance);

plot(xr, xr*a + b, '-', distance, y, '.', 'markersize', 25);
pause;

% Normalize with sqrt.
y = sqrt(length);
x = A \ y';

% Residuals.
corrcoef(distance, y)

% Plot.
b = x(1, 1);
a = x(2, 1);
xr = min(distance):max(distance);

plot(xr, xr*a + b, '-', distance, y, '.', 'markersize', 25);
pause;

% Normalize with y^(2/3).
y = length.^(2/3);
x = A \ y';

% Residuals.
corrcoef(distance, y)

% Plot.
b = x(1, 1);
a = x(2, 1);
xr = min(distance):max(distance);

plot(xr, xr*a + b, '-', distance, y, '.', 'markersize', 25);
pause;
