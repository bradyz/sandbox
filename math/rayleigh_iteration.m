function [c, v] = rayleigh_iteration(A, initial)
% Solves for eigenpair of A using rayleigh quotient and inverse power method.
%
% Params:
%   A: m x m matrix, non-defective.
%   initial: float, initial seed for eigenvalue.
%
% Returns:
%   c: float, the closest eigenvalue.
%   v: (m x 1), a corresponding eigenvector.

EPSILON = 1e-7;
MAX_ITERATIONS = 1e6;

[m, ~] = size(A);

v = rand(m, 1);
c = initial;

for i = 1:MAX_ITERATIONS
    % Apply one step of inverse power method.
    w = inv(A - c * eye(m)) * v;

    v = w / norm(w);
    c = v' * A * v;

    if norm(A * v - c * v) < EPSILON
        i
        break;
    end
end

end
