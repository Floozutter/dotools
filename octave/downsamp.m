pkg load signal;

args = argv();
ifilename = args{1};
ofilename = args{2};
scale = str2num(args{3});

[data, fs] = audioread(ifilename);
audiowrite(ofilename, resample(data, 1, scale, 1), fs / scale);
