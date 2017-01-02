DIMENSIONS = 10;
NUM_CLUSTERS = 20;
POINTS_PER_CLUSTER = 100;
RELATIVE_JITTER = 0.25;

n = NUM_CLUSTERS * POINTS_PER_CLUSTER;
clusters_XD = randn(DIMENSIONS, NUM_CLUSTERS);
points_XD = zeros(DIMENSIONS, n);

% Generate points_XD around the clusters.
for i = 1:n
    cluster = clusters_XD(:, randi(NUM_CLUSTERS));
    jitter = randn(DIMENSIONS, 1);
    jitter = jitter / (norm(jitter) / (RELATIVE_JITTER * norm(cluster)));

    points_XD(:, i) = cluster + jitter;
end

[U, S, V] = svd(points_XD, 'econ');

% Project down into 3D space.
points_3D = zeros(3, n);
clusters_3D = zeros(3, NUM_CLUSTERS);

% Take the dot products with the three most principle axes.
for i = 1:n
    points_3D(:, i) = U(:, 1:3)' * points_XD(:, i);
end

for i = 1:NUM_CLUSTERS
    clusters_3D(:, i) = U(:, 1:3)' * clusters_XD(:, i);
end

clf;
scatter3(points_3D(1, :), points_3D(2, :), points_3D(3, :), 'c');
hold on;
scatter3(clusters_3D(1, :), clusters_3D(2, :), clusters_3D(3, :), ...
         'r', 'filled');
