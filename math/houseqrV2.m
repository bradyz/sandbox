function [Q, R] = houseqr(A)
% Decomposes a matrix A into Q, orthogonal and R, upper triangular.
% This uses householder reflections.
%
% Params:
%   A: m x n matrix, full rank.
%
% Returns:
%   Q: m x m matrix, orthogonal, spans A.
%   R: m x n matrix, upper triangular.

function u = reflect(w, v)
% Returns the vector orthogonal to hyperplane to reflect across, so we can
% create I - 2uu' = H, such that Hw = +/- ||w||v.
%
% Params:
%   w: n x 1 vector, the input vector.
%   v: n x 1 unit vector, the vector to reflect to.
%
% Returns:
%   u: n x 1 vector, the vector orthogonal to the hyperplane.

% This is the u that projects w "further". Used to avoid subtraction.
u = w + sign(w(1)) * norm(w) * v;
u = u / norm(u);
end

[m, n] = size(A);

% Going to hit A with a bunch of reflector matrices.
R = A;
Q = eye(m);

for i = 1:n
    % Current dimension.
    d = m - i + 1;

    % Want to make R(i:m, i) only have a component in first dimension.
    u = reflect(R(i:m, i), eye(d, 1));
    H = eye(d) - 2 * u * u';

    % Align the lower part of R.
    R(i:m, i:n) = H * R(i:m, i:n);

    % This is the full reflector matrix.
    H_m = eye(m);
    H_m(i:m, i:m) = H;

    % We have H_n * ... * H_2 * H_1 * A = R.
    % Since H_i full rank, A = H_1^-1 * H_2^-1 * ... * H_n^-1 * R.
    % Since H_i unitary, A = H_1 * H_2 * ... * H_n * R.
    Q = Q * H_m;
end
end
