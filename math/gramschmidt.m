function [Q, R] = gramschmidt(A, flag)
% Decomposes a matrix A into Q, orthogonal and R, upper triangular.
%
% Params:
%   A: m x n matrix, full rank.
%   flag: [0, 1], 0 for classical, 1 for modified.
%
% Returns:
%   Q: m x n matrix, orthogonal, spans A.
%   r: n x n matrix, upper triangular.

[m, n] = size(A);

Q = zeros(m, n);
R = zeros(n, n);

for j = 1:n
    V(:, j) = A(:, j);
    for i = 1:j-1
        if flag == 1
            R(i, j) = Q(:, i)' * A(:, j);
        else
            R(i, j) = Q(:, i)' * V(:, j);
        end
        V(:, j) = V(:, j) - R(i, j) * Q(:, i);
    end
    R(j, j) = norm(V(:, j));
    Q(:, j) = V(:, j) / R(j, j);
end
