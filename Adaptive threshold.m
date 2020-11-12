% hy1dist should be found in previous sections. 

%%
%Performing local thresholding, save binary filter images in DYs. 
DYs = false(size(BG));
sen = 0.5;
parfor i = 1:num_images_2
ad_thresh = adaptthresh(I(:,:,i), sen);
DYs(:,:,i) = imbinarize(I(:,:,i),ad_thresh);
end
%
%Have a look at the first image to make sure nothing goes wrong: 
Result = I(:,:,1).*uint8(DYs(:,:,1));
imwrite(Result,[outpath 'Gconv_filter' '.tif']);
