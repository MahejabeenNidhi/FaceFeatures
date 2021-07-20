ds = load('COFW_test.mat');
for I = 1:length(ds.IsT)
    fileName = string(I);
    imageExt = '.jpg';
    name = strcat(fileName, imageExt);
    ImgArray = ds.IsT{I, 1};
    imwrite(ImgArray, name);
end


    