n=100; % the number of sample points
X=8*rand(n,1); %generate n values in [0,8]
Y=-1 + 2*rand(n,1); %generate n values in [-1,1]
Rp=0; %initialize ratio of points that are in the "positive" area
Rm=0; %initialize ratio of points that are in the "negative" area
for i=1:n
    if g(X(i,1))>=0 && Y(i,1)>=0 && Y(i,1)<=g(X(i,1))
        Rp = Rp +1;
    end
    if g(X(i,1))<=0 && Y(i,1)<=0 && Y(i,1)>=g(X(i,1))
        Rm = Rm +1;
    end
end
ratio = (Rp - Rm)/n;
integ = ratio*16;
sigma =  sqrt(ratio*(1-ratio)/n); %the std of the integral knowing the sampling  
p = 0.95;
q=erfinv(p)*sqrt(2);
t1 = ratio - sigma*q;
t2 = ratio + sigma*q;
disp(['the area is ', num2str(integ), ' with ', num2str(p), ' level confidence interval: [', num2str(t1*16), ', ', num2str(t2*16), ']']);

fh = @g;
RiemannSum(fh, 0, 8, 100) %Riemann Sum algorithm to compare

function y=g(x)
    y = sin(1+log(x));
end

function val = RiemannSum(func, inf, sup, N)
    val = 0;
    base=(sup-inf)/N;
    t=linspace(inf, sup, N+1);
    for i=1:N
        mid = t(i) + base/2;
        high = func(mid);
        val = val + high*base;
    end

end

