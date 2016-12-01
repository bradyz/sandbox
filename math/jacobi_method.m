% This linear solver tries to solve Ax = b by breaking up A = (D + R).
% <=> (D + R)x = b.
% This is because D is "easier" to invert (recipricols).
%
% We want to solve Ax = b.
% A in n x n, convergence criterion below.
% x in n x 1.
% b in n x 1.
% The goal is to find an x in R^{n} such that ||Ax - b|| is minimized.
%
% Converges IFF norm(D^-1 R) < 1.
% A sufficient condition is also that |a_ii| > \Sigma_1_{n} |a_ij|, for all i.

% Metadata.
n = 4;
eps = 1e-10;

% Want to solve: Ax = b.
A = [10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0, 3 -1 8]

% Find some b to solve for.
b = [6 25 -11 15]'

% Set up D (which is "easy" to invert).
D = eye(n) .* A;
D_inv = inv(D);
R = A - D;

% Set initial guess.
tmp = 0;
x_k = b;
k = 1;

while norm(x_k - tmp) > eps * norm(b)
    tmp = x_k;
    x_k = D_inv * (b - R * tmp);
    k = k + 1;
end

% Took k iterations.
k
norm(A * x_k - b)
