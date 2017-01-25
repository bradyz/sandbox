%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 1d.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = 100;

s = 1e-5;
A = rand(n, n);
q = rand(n, 1);
w = rand(n, 1);

% Make A symmetric.
for i=1:n
    for j=i:n
        A(j, i) = A(i, j);
    end
end

f_1 = .5 * q' * A * q;
f_2 = .5 * (q + s * w)' * A * (q + s * w);

% Numerical solution.
r_1d = (f_2 - f_1) ./ s;

% Analytic solution.
a_1d = q' * A * w;

fprintf('Problem 1d: %0.10f\n', norm(r_1d - a_1d) / norm(r_1d));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 2a.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = 100;

s = 1e-5;
A = rand(n, n);
q = rand(n, 1);
b = rand(n, 1);
w = rand(n, 1);

f_1 = norm(A * q - b)^2;
f_2 = norm(A * (q + s * w) - b)^2;

% Numerical solution.
r_2a = (f_2 - f_1) / s;

% Analytic solution.
a_2a = 2 * (A * q - b)' * (A * w);

fprintf('Problem 2a: %0.10f\n', norm(r_2a - a_2a) / norm(r_2a));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 2b.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = 100;

s = 1e-5;
A = rand(n, n);
B = rand(n, n);

f_1 = trace(A);
f_2 = trace(A + s * B);

% Numerical solution.
r_2b = (f_2 - f_1) ./ s;

% Analytic solution.
a_2b = trace(B);

fprintf('Problem 2d: %0.10f\n', norm(r_2b - a_2b) / norm(r_2b));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 2c.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
s = 1e-2;

q = randn(3, 1) * 1e4;
w = randn(3, 1);

% Numerical solution.
u = @fu;
v = @fv;
du = @dfu;
dv = @dfv;

f_1 = norm(cross(u(q), v(q)));
f_2 = norm(cross(u(q + s * w), v(q + s * w)));
r_2c = (f_2 - f_1) ./ s;

% Analytic solution.
a = cross(u(q), v(q))' * (cross(du(q, s, w), v(q)) + cross(u(q), dv(q, s, w)));
b = norm(cross(u(q), v(q)));
a_2c = a / b;

fprintf('Problem 2c: %0.10f\n', norm(r_2c - a_2c) / norm(r_2c));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 2d.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
s = 1e-5;

u = rand(3, 1);
v = rand(3, 1);
w = rand(3, 1);

q = rand(3, 1);
dq = rand(3, 1);

f_1 = 1 / 6 * (cross(u - q, v - q))' * (w - q);
f_2 = 1 / 6 * (cross(u - (q + s * dq), v - (q + s * dq)))' * (w - (q + s * dq));

% Numerical solution.
r_2d = (f_2 - f_1) / s;

% Analytic solution.
a_2d = -1 / 6 * (cross(u - q, dq)'    * (w - q) + ...
                 cross(dq, v - q)'    * (w - q) + ...
                 cross(u - q, v - q)' * (dq));

fprintf('Problem 2d: %0.10f\n', norm(r_2d - a_2d) / norm(r_2d));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Functions for Problem 2c.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function x = fu(q)
    x = q / norm(q) + [0, 1, 0]';
end

function x = fv(q)
    x = q / norm(q) + [1, 0, 0]';
end

function x = dfu(q, s, w)
    x = (fu(q + s * w) - fu(q)) ./ s;
end

function x = dfv(q, s, w)
    x = (fv(q + s * w) - fv(q)) ./ s;
end
