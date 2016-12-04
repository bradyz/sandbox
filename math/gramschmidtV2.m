function [Q, R] = gramschmidtV2(A)
% Decomposes a matrix A into Q, orthogonal and R, upper triangular.
%
% Params:
%   A: m x n matrix, full rank.
%
% Returns:
%   Q: m x n matrix, orthogonal, spans A.
%   r: n x n matrix, upper triangular.

[m, n] = size(A);

Q = zeros(m, n);
R = zeros(n, n);

% First want to construct the orthonormal part.
for i = 1:n
    v = A(:, i);

    % Subtract off bits already spanned by Q.
    for j = 1:i-1
        v = v - Q(:, j) * Q(:, j)' * A(:, i);
    end

    % Now we know this v is orthogonal to previous q_i.
    Q(:, i) = v / norm(v);
end

% Now fill in the coefficients. R(:, i) tells us how much Q we need.
for j = 1:n
    for i = 1:j
        R(i, j) = A(:, j)' * Q(:, i);
    end
end
