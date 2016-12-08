function [c, v] = power_iteration(A)
% Solves for the largest eigenvalue of A.
%
% Params:
%   A: m x m matrix, non-defective.
%
% Returns:
%   c: float, the largest eigenvalue.
%   v: (m x 1), a corresponding eigenvector.

EPSILON = 1e-7;
MAX_ITERATIONS = 1e6

[m, ~] = size(A);

v = rand(m, 1);
c = 1;

for i = 1:MAX_ITERATIONS
    v = (A * v);
    v = v / norm(v);
    c = v' * A * v;

    if norm(A * v - c * v) < EPSILON
        break;
    end
end

end
