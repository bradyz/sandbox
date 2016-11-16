data = load('Q2.mat');

% Investigate error in solution by perturbing A and b.
A = data.A;
b = data.b;
tau = 1e-4;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 1a: Find (A + dA) s.t. error in x is maximized.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[U, S, V] = svd(A);

% Want to make A lose rank.
dA = U * [0 0; 0 0; 0 -tau * S(1, 1)] * V;
% dA = [zeros(3, 1) -tau * S(1, 1) * U(:, 3)];

% sigma_1 and sigma_2 tell us that the conditioning of (A + dA) is worse.
A_prime = A  + dA;
[U_prime, S_prime, V_prime] = svd(A_prime);

% Relative error is ~11%.
x = inv(A' * A) * A' * b;
xp = inv(A_prime' * A_prime) * A_prime' * b;
dx1 = norm(x - xp, 2) / norm(x, 2);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Problem 1b: Find (b + db) s.t. error in x is maximized.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[U, S, V] = svd(A);

% Want to push all the energy into the direction that is "poorly" spanned.
db = tau * norm(b, 2) * U(:, 2);

% Relative error is ~20%.
x = inv(A' * A) * A' * b;
xp = inv(A' * A) * A' * (b + db);
dx2 = norm(x - xp, 2) / norm(x, 2);
