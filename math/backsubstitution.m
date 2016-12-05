function x = backsubstitution(R, b)
% Solves the system Rx = b, where R is upper triangular.
% This algorithm is backwards stable.
%
% Params:
%   R: m x m matrix, upper triangular (non zero on diagonals).
%   b: m x 1 vector.
%
% Returns:
%   x: m x 1 vector, the solution to the system.
[m, ~] = size(R);

x = zeros(m, 1);

for i = m:-1:1
    % Use the previous answers.
    x(i) = b(i);
    for j = m:-1:i+1
        x(i) = x(i) - R(i, j) * x(j);
    end

    % Solve for one variable.
    x(i) = x(i) / R(i, i);
end

end
