Image Denoising

The goal of this problem is to recover the clean image from a noisy input. The graphical model we use is a pairwise MRF. A pixel has four neighbors. 
We are going to use Markov Random Fields (MRFs) to model the distribution of natural images and restore the clean image given a noisy input image. 
 
Solution: 
To denoise the image we need to use the given energy function and initially need to guess the values for h, beta and eta.
After experimentation I have finalized the values as below:
h = 0.1
beta = 2
eta = 0.1
Given image is a binary image where pixel values belongs to {1, -1 }.
Lambda function : 
neighbors  will return all the neighbors of a pixel.
energy function: 
will call summation function to get the value of   and will return the energy for the given pixel.
Now for each pixel in the image I am calling the energy function twice. 1st time with original value of the pixel and 2nd time for the flipped value of the pixel. After getting both energies we will choose the pixel value which gives the low energy.
Keep doing this for the image again and again until there is 0 number of flips in a full iteration.

For the below given code we are able to get the denoised image with 99.38 similarity the original clean image. (Converges after 5 Iteration as given in the below screen shot)
