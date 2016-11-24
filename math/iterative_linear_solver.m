% This linear solver takes the inspiration from Euler's method for solving
% differential equations.
%
% We want to solve Ax = b, and we are given A in R^{m, n} and b in R^{m}.
% The goal is to find an x in R^{n} such that ||Ax - b|| is minimized.
%
% The following scheme is applied -
% x_0 = A^T * b.
% r_k = (beta * I + A^T * A) * x - A^T * b.
% x_{k+1} = x_k + delta * r_k.
% And iterate until ||x_{k+1} - x_k|| < epsilon.

% Metadata.
m = 5;
n = 3;
eps = 1e-5;
delta = 1e-6;
alpha = 1e-10;

% Want to solve: Ax = b.
A = randn(m, n);
b = randn(m, 1);

% Save some intermediate calculations.
beta_I = alpha * eye(n);
AT_A = A' * A;
AT_b = A' * b;

% Intialize guesses.
x_a = AT_b;
x_b = x_a + delta * ((beta_I + AT_A) * x_a - AT_b);

% Until convergence, step.
while norm(x_b - x_a) > eps
    norm(x_b - x_a)
    x_a = x_b;
    x_b = x_a + delta * ((beta_I + AT_A) * x_a - AT_b);
end
