% QR Decomposition (A = QR).
% A is m x n, full rank.
% Q is m x n unitary, spans A.
% R is n x n upper triangular.

% Basic test.
m = 4;
n = 2;
A = rand([m, n]);

% Get full QR decomposition (M x M, M x N)
[Q, R, U] = houseqr(A);

% Get matlab QR decomposition.
[Q_p, R_p] = qr(A);

% Inspect.
A
Q * R

% Exercise 10.3, Trefethen.
Z = [1 2 3; 4 5 6; 7 8 7; 4 2 3; 4 2 2];
[Q, R, U] = houseqr(Z);

% Inspect.
Z
Q * R

% Inspect H_1 A, H_2 * H_1 * A, H_3 * H_2 * H_1 * A.
[m, n] = size(Z);

for i = 1:3
    H_i = eye(m);
    for j = 1:i
        u = U(:, j);
        H_j = eye(m) - 2 * u * u';
        H_i = H_j * H_i;
    end
    H_i * Z
    keyboard
end
