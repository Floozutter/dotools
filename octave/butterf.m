pkg load signal;

args = argv();
ifilename = args{1};
ofilename = args{2};
ftype = args{3};
order = str2num(args{4});
cutoff = str2num(args{5});

[src, fs] = audioread(ifilename);
wn = @(cutoff) cutoff / (fs/2);
[b, a] = butter(order, arrayfun(wn, cutoff), ftype);
audiowrite(ofilename, filter(b, a, src), fs);
