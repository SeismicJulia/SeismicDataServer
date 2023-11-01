# 2D Acoustic Frequency-domain FWI

This is a 2D full waveform inversion code using simultaneous encoded sources based on first- and second-order optimization methods developed in [Amsalu's Thesis](https://saig.physics.ualberta.ca/lib/exe/fetch.php?media=publications:theses:2014_amsalu_phd.pdf){target="_blank"}.

Forward modelling: solves a two-dimensional wave-equation in frequency domain
$$
\frac{\partial }{\partial x}\left(\frac{1 }{\rho}\frac{\partial }{\partial x} p(\omega) \right) +\frac{\partial }{\partial z}\left(\frac{1}{\rho}\frac{\partial }{\partial z} p(\omega) \right) + \frac{\omega^2}{\kappa} p(\omega) =  f(\omega)
$$
where, $\kappa = \rho v^2$  is the bulk modulus, $\rho $  is the density, $v$ is the velocity, $p$ is the pressure field,  $\omega$ is the angular frequency and $f(\omega)$ is the source signature. 

After discretizating,  the acoustic wave equation can be written in a compact  matrix form as  
$$
A({\bf x}, {\bf m}, \bf \omega){\bf p}({\bf x }, {\bf x}\_{s},\omega) ={\bf f(\omega)} \delta({\bf x} - {\bf x}\_{s}),
$$
where $ A({\bf x}, {\bf m}, \omega) $ is the discretized Helmholtz equaton, $ {\bf p}( {\bf x}, {\bf x}\_{s},\omega) $ is a complex pressure field for a shot located at $ {\bf x}\_{s} $.