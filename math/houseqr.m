function [Q_reduced, R_reduced, U_reduced] = houseqr(A)
% Decomposes a matrix A into Q, orthogonal and R, upper triangular.
% This uses householder reflections.
%
% Params:
%   A: m x n matrix, full rank.
%
% Returns:
%   Q: m x n matrix, orthogonal, spans A.
%   R: n x n matrix, upper triangular.
%   U: m x n matrix, reflector vectors.

function u = reflect(w, v)
% Returns the vector orthogonal to hyperplane to reflect across.
%
% Params:
%   w: n x 1 vector, the input vector.
%   v: n x 1 unit vector, the vector to reflect to.
%
% Returns:
%   u: n x 1 vector, the vector orthogonal to the hyperplane.

% This is the u that projects w "further".
u = sign(w(1)) * norm(w) * v + w;

% This u can be degenerate. DO NOT USE.
% u = w - norm(w) * v;

u = u / norm(u);
end

function [Q, R, U] = houseqrfull(A)
[m, n] = size(A);

% Canonical basis vector for R^m.
e1 = zeros(m, 1);
e1(1) = 1;

% Align first column of A with e1.
u = reflect(A(:,1), e1);

% Householder matrix that projects v across hyperplane.
H = eye(m) - 2 * u * u';

% Apply Householder to A.
B = H * A;

if n == 1
    % Base case.
    [m, n] = size(A);
    R = [B(1, :); zeros(m-1, 1)];
    U = u;
else
    % Recurse on lower right corner of A.
    [Q_p, R_p, U_p] = houseqrfull(B(2:m, 2:n));

    % Use recursive solution from lower right corner of A.
    [m, n] = size(A);
    R = [B(1, :); [zeros(m-1, 1), R_p]]
    keyboard;
    U = [u, [zeros(1, n-1); U_p]];
end

% Product of H_1 H_2 ... H_N.
Q = eye(m, m);

for i = 1:n
    u_i = U(:, i);
    H_i = eye(m) - 2 * u_i * u_i';
    Q = Q * H_i;
end

end

% Get full QR and then reduce.
[Q_reduced, R_reduced, U_reduced] = houseqrfull(A);

% Reduce to (M x N, N x N) by culling zeros off R.
[m, n] = size(A);
Q_reduced = Q_reduced(:, 1:n);
R_reduced = R_reduced(1:n, :);

end
