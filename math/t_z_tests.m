%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Data setup.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
filepath = '/Users/bradyzhou/Downloads/DieData1.txt';
table = struct2cell(tdfread(filepath));

% table is n x 5, since there are 5 die.
table = [table{:}];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Test setup.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
alpha = 0.05;
[num_rows, num_dice] = size(table);

% Want to see what conclusions we can make at different sample sizes.
sample_sizes = [200 1000 num_rows];

for i = 1:size(sample_sizes, 2)
    % Go through 200, 1000, all samples.
    sample_size = sample_sizes(i)

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Using t-test for means.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Stderr is std_y / n.
    table_stderr = std(table) / sqrt(sample_size);

    % T-statistic is defined as (y_bar - expected(y)) / stderr_y.
    table_t = (mean(table) - 3.5) ./ table_stderr;

    % Make all the values negative so we can do cdf of [-inf, x].
    table_t = -1 * sign(table_t) .* table_t;

    % Two tailed test so we have to multiple p by 2.
    t_p_value = 2 * tcdf(table_t, sample_size-1)

    % We reject the null hypothesis if the p-value falls under alpha.
    t_reject_ho = t_p_value < alpha

    % Look at t-test.
    % pause

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Using z-test for proportions.
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % Go through each dice and find the proportion that each value occurs.
    for col = 1:num_dice
        counts = tabulate(table(1:sample_size, col));
        proportions(col, :) = counts(:, 3) * 0.01;
    end

    % Populate z-statistics for each proportion.
    sd_p = sqrt((1 / 6) * (5 / 6) / sample_size);
    z = -abs((proportions - 1 / 6) / sd_p);

    % The distribution is two-tailed.
    z_p_value = 2 * normcdf(z)

    % We reject the null hypothesis that the proportion of a value is unbias.
    z_reject_ho = z_p_value < alpha

    % Look at z-test.
    % pause;
end
