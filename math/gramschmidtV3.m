function [Q, R] = gramschmidtV3(A)
% Full QR decomposition.
% Decomposes a matrix A into Q, orthogonal and R, upper triangular.
%
% Params:
%   A: m x n matrix, full rank.
%
% Returns:
%   Q: m x m matrix, orthonormal, spans R^m.
%   r: m x n matrix, upper triangular.

[m, n] = size(A);

Q = zeros(m, m);
R = zeros(m, n);

% First want to construct the orthonormal part.
for i = 1:m
    if i < n+1
        v = A(:, i);
    else
        % Picking a random vector is almost guaranteed to not lay in span.
        v = rand(m, 1);
    end

    % Subtract off bits already spanned by Q.
    for j = 1:i-1
        v = v - Q(:, j) * Q(:, j)' * v;
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
