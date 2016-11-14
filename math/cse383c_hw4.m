x=2.^[-30:2:1]

% Showing how f(x) = x - sin(x) behaves.
kappa = abs(1 - cos(x)).*abs(x)./abs(x - sin(x));

% Plot.
loglog(x, y1, 'linewidth', 2);
pause;

% Different associativity causes different rounding errors.
f = x - sin(x);
q = (x - x) - ((x.^3.0/6.0).*(1-(x.^2./20.0).*(1-(x.^2./42).*(1-x.^2./72))))

% Plot.
loglog(x, abs(f - q)./abs(q), 'linewidth', 3)
pause;
