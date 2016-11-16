function l_curve(A, b, tau, xstar)

[U, S, V] = svd(A);
[m, n] = size(A);
sigma = diag(S);

points = [];

for i = 1:size(sigma, 1)
    beta_i = sigma(i);
    b_hat = U' * b;
    x_hat = zeros(n, 1);
    k = min(m, n);
    x_hat(1:k) = (sigma(1:k).^2)./(sigma(1:k).^2 + beta_i).*b_hat(1:k)./sigma(1:k);
    x_prime = V * x_hat;

    points = [points; norm(A * x_prime - b) norm(x_prime)];
end

figure;
loglog(points(:, 1), points(:, 2));
