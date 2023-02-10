## Rayleigh Jeans Law:
---
The Rayleigh-Jeans law is an approximation of the Planck law for low frequencies. It is used to calculate the blackbody radiation emitted by a body at a given temperature. The Rayleigh-Jeans law is an approximation of the Planck law for low frequencies. It is used to calculate the blackbody radiation emitted by a body at a given temperature.  
The term **Black body radiation** esentially refers to the radiation emitted by a body at a temperature above absolute zero. The radiation emitted by a black body is called **black body radiation** because it is emitted in all directions and is not absorbed by the body. It is calculated as the `energy density per unit frequency/wavelength`. 

$$
n_{\nu} = \frac{8 \pi \nu^2}{c^2}   
$$
where $n_\nu$ is the number of oscillations per unit volume in a frequency range of $\nu$ to $\nu + d\nu$ and $c$ is the speed of light.

$$
u_\nu = \frac{E_{total}}{V} = \frac{N\bar{E}}{V}

$$
where $u_\nu$ is the energy density per unit frequency, $\bar{E}$ is the average energy associated with each oscillation, $N$ is the number of oscillations in the frequency range of $\nu$ to $\nu + d\nu$  and $V$ is the volume.


**Partition Function** = $Z = \sum_{i=1}^{N} e^{-\frac{E_i}{kT}}$  
where $E_i$ is the energy of the $i^{th}$ state, $k$ is the Boltzmann constant and $T$ is the temperature.

$$
\text{Average energy} \;\; \bar{E} =  
\frac{\sum_{i=1}^{N} E_i e^{-\frac{E_i}{kT}}}{\sum_{i=1}^{N} e^{-\frac{E_i}{kT}}}
$$

## Rayleigh's Assumption:
- Energy is continuous and NOT discrete which changes the formula for average energy into an integral instead of a sum.

$$
\text{Average energy} \;\; \bar{E} = \frac{
\int_{0}^{\infty} E e^{-\frac{E}{kT}} dE}
{\int_{0}^{\infty} e^{-\frac{E}{kT}} dE}

 = kT
$$

$$ 
\therefore u_\nu = \frac{8 \pi \nu^2 kT}{c^3}
$$
The term $c^3$ is the volume of a small box of size c

Therefore, we see that $u_\nu$ is proportional to $\nu^2$ and proportional to $T$. This is the Rayleigh-Jeans law.

However, this is wrong as the curve diverges at higher Temperatures from the actual experimental curve. This is because the Rayleigh-Jeans law assumes that the energy is continuous and not discrete. This is not true as the energy is discrete and the average energy is not equal to $kT$. This is called `ultraviolet catastrophe`.

---
## Planck's Law:
---

### Planck's Assumption:
- Energy is discrete and NOT continuous.
Energy CANNOT be excreted by matter in a continuous fashion.

$$
E = nh\nu, \;\;\;\; n = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
$$
**Partition Function:**
$$
Z = \sum_{n=0}^{\infty} e^{-\frac{nh\nu}{kT}} \\

\text{Average energy} \;\; \bar{E} = \frac{\sum E_i e^{-\frac{E_i}{kT}}}{\sum e^{-\frac{E_i}{kT}}} 


= \frac{\sum nh\nu e^{-\frac{nh\nu}{kT}}}{\sum e^{-\frac{nh\nu}{kT}}} \\
= \frac{h\nu}{e^{\frac{h\nu}{kT}} - 1}
$$

$$
u_\nu = \frac{8 \pi \nu^2 kT}{c^3} \frac{h\nu}{e^{\frac{h\nu}{kT}} - 1}
$$

This is in accordance with the experimental data. The Planck law is the correct law for black body radiation. The Rayleigh-Jeans law is an approximation of the Planck law for low frequencies.

---
 


## References:
- [Rayleigh-Jeans Law](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Jeans_law)
- [Planck's Law](https://en.wikipedia.org/wiki/Planck%27s_law)
- [Black Body Radiation](https://en.wikipedia.org/wiki/Black-body_radiation)

