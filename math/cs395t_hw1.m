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
r_1d = (f_2 - f_1) ./ s

% Analytic solution.
a_1d = q' * A * w

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
r_2a = (f_2 - f_1) / s

% Analytic solution.
a_2a = 2 * (A * q - b)' * (A * w)

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
r_2b = (f_2 - f_1) ./ s

% Analytic solution.
a_2b = trace(B)

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
r_2d = (f_2 - f_1) / s

% Analytic solution.
a_2d = -1 / 6 * (cross(u - q, dq)'    * (w - q) + ...
                 cross(dq, v - q)'    * (w - q) + ...
                 cross(u - q, v - q)' * (dq))
