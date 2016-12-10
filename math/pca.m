IMAGE = '~/Desktop/icpc.png';

im = imresize(rgb2gray(imread(IMAGE)), 0.5);
A = double(im);
[m, n] = size(A);

[U, S, V] = svd(A, 'econ');

B = zeros(m, n);

for i = 1:size(S, 1)
    B = B + U(:, i) * S(i, i) * V(:, i)';

    if mod(i, 10) == 0
        imshow(uint8(B));
        pause;
    end
end

