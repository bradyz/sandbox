function [best_beta] = cross_validation(A, b, tau, xstar)

[U, S, V] = svd(A);
[m, n] = size(A);
sigma = diag(S);

best_beta = sigma(1);
best_E = Inf;

for i = 1:size(sigma, 1)
    beta_i = sigma(i);

    A_pinv = inv(A' * A + beta_i * eye(n)) * A';
    E = norm((eye(m) - A * A_pinv) * beta_i)^2 / trace(eye(m) - A * A_pinv)^2;

    if E < best_E
        best_E = E;
        best_beta = beta_i;
    end
end
