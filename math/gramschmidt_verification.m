function epsilon = gramschmidt_verification(Q)
% Finds the greatest inner product between the column vectors.
%
% Params:
%   Q: m x n matrix, the Q from a QR decomposition.
%
% Returns:
%   epsilon: a scalar.

[m, n] = size(Q);

epsilon = 0;

for i = 1:n
    for j = i+1: n
        epsilon = max(epsilon, Q(:, i)' * Q(:, j));
    end
end
