p1 = rand(2, 1);
p2 = rand(2, 1);
p3 = rand(2, 1);

plot(p1(1, 1), p1(2, 1), 'r+');
hold on;

plot(p2(1, 1), p2(2, 1), 'r+');
hold on;

plot(p3(1, 1), p3(2, 1), 'g+');
hold on;

% Projector to span of v.
v = (p2 - p1) / norm(p2 - p1);
P = v * v';

% Project p3 and offset again.
z = P * (p3 - p1) + p1;

plot(z(1, 1), z(2, 1), 'b+');

ylim([-2 2]);
xlim([-2 2]);
