function gramschmidt_compare(A)
% Uses different QR decomposition algorithms and tests for numerical error.
%
% Params:
%   A: m x n matrix, full rank

% Compare.
[Q1, R1] = gramschmidt(A, 1);
[Q2, R2] = gramschmidt(A, 0);
[Q3, R3] = qr(A);

% Tests "worst" orthogonality.
r1 = gramschmidt_verification(Q1);
r2 = gramschmidt_verification(Q2);
r3 = gramschmidt_verification(Q3);

fprintf('Classical:\t%d\nModified:\t%d\nMatlab:\t\t%d\n\n', r1, r2, r3);
