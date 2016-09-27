x = 1:1000;

m358k_helper(x, x.^2);
m358k_helper(x, x.^3);
m358k_helper(x, x.^4);
m358k_helper(x, x.^5);

m358k_helper(x, log(x.^2));
m358k_helper(x, log(x.^3));
m358k_helper(x, log(x.^4));
m358k_helper(x, log(x.^5));

m358k_helper(log(x), log(x.^2));
m358k_helper(log(x), log(x.^3));
m358k_helper(log(x), log(x.^4));
m358k_helper(log(x), log(x.^5));
