% QR Decomposition (A = QR).
% This program demonstrates numerical errors.
% A is m x n, full rank.
% Q is m x n orthogonal, spans A.
% R is n x n upper triangular.

% Basic test.
A = rand([5, 3]);
gramschmidt_compare(A);

% Numerical error test.
e = 1e-9;
A = [[1, e, 0, 0]', [1, 0, e, 0]', [1, 0, 0, e]'];
gramschmidt_compare(A);

% Svd test.
kappa = [1, 1e3, 1e6, 1e9];
for i = 1:size(kappa, 2)
    A = gallery('randsvd', 100, kappa(i));
    fprintf('Kappa: %d\n', kappa(i));
    gramschmidt_compare(A);
end
