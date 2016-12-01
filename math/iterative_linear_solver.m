% This linear solver takes the inspiration from Euler's method for solving
% differential equations.
%
% We want to solve Ax = b.
% A in n x n, symmetric positive definite (done by B' * B for B full rank).
% x in n x 1.
% b in n x 1.
% The goal is to find an x in R^{n} such that ||Ax - b|| is minimized.

% Metadata.
m = 5;
n = 3;
eps = 1e-10;
delta = 1e-2;

% Want to solve: Ax = b.
A = rand(m, n);
A = A' * A;
b = rand(n, 1);

% Set initial guess.
tmp = 0;
x_k = b;
k = 1;

while norm(x_k - tmp) > eps * norm(b)
    % tmp is x_k-1.
    tmp = x_k;
    x_k = tmp + delta * (b - A * tmp);
    k = k + 1;
end

% Took k iterations.
k
norm(A * x_k - b)
