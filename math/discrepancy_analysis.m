function [best_beta] = discrepancy_analysis(A, b, tau, xstar)

[U, S, V] = svd(A);
[m, n] = size(A);
sigma = diag(S);

best_beta = sigma(1);
best_diff = Inf;

for i = 1:size(sigma, 1)
    beta_i = sigma(i);
    b_hat = U' * b;
    x_hat = zeros(n, 1);
    k = min(m, n);
    x_hat(1:k) = (sigma(1:k).^2)./(sigma(1:k).^2 + beta_i).*b_hat(1:k)./sigma(1:k);
    x_prime = V * x_hat;

    diff = abs(norm(A * x_prime - b) - tau * norm(b));
    if diff < best_diff
        best_diff = diff;
        best_beta_i = beta_i;
    end
end
