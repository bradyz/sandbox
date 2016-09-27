% Planet data.
distance = [36 67 93 142 474 776 1784 2796 3707];
length = [0.24 0.61 1.00 1.88 11.86 29.46 84.07 164.82 247.68];

% Find correlation based on distance.
m358k_helper(distance, length);
m358k_helper(distance, log(length));
m358k_helper(distance, sqrt(length));
m358k_helper(distance, length.^(2/3));

% Find correlation based on position.
position = [1 2 3 4 5 6 7 8 9];

m358k_helper(position, distance);
m358k_helper(position, log(distance));
m358k_helper(position, sqrt(distance));
m358k_helper(log(position), log(distance));

% Find correlation based on updated position.
position = [1 2 3 4 5 7 8 9 10];

m358k_helper(position, distance);
m358k_helper(position, log(distance));
m358k_helper(position, sqrt(distance));
m358k_helper(log(position), log(distance));
