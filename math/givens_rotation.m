function [Q, R] = givens_rotation(A)
% Solves A = QR, where Q is unitary, R is upper triangular.
%
% Params:
%   A: m x n matrix, full rank.
%
% Returns:
%   Q: m x m matrix, orthogonal, spans A.
%   R: m x n matrix, upper triangular.
[m, n] = size(A);

% Q is the product of these rotations.
Q = eye(m);

% Gonna hit A with a bunch of rotations to make R upper triangular.
R = A;

for i = 1:n
    % Want to make zero out entries i+1 to m of column i for R.
    for j = i+1:m
        % [ c    -s] [x] = [z]
        % [+s     c] [y]   [0]
        x = R(i, i);
        y = R(j, i);

        % cos(theta) and sin(theta) are just the normalized component.
        c = x / norm([x y]');
        s = y / norm([x y]');

        % Align the two entries using Givens matrices.
        G = eye(m);
        G(i, i) =  c; G(i, j) = +s;
        G(j, i) = -s; G(j, j) =  c;

        % R = G_n ... G_2 G_1 A.
        R = G * R;

        % A = G_1 G_2 ... G_n R.
        % Since G_i unitary, so Q = G_1' G_2' ... G_n'.
        Q = Q * G';
    end
end

end
