# Isomers and Decays

## Background

### Elements, Isotopes and Isomers

At the centre of every atom lies its nucleus. A nucleus is comprised of protons and neutrons, collectively known as nuclides. Normally rhese nuclides sit in the lowest energy configuration available to them, known as its "ground state". Sometimes, though, these nuclides are arranged in one of a number of higher energy configrations, known as "excited states". Dependent on the number of different nuclides and their energy state, the nucleus will have different properties. We'll begin with some basic definitions to help our discussion:

* Atomic number: describes the number of protons in a nucleus.
* Atomic mass: describes the number nuclides (protons + neutrons) in a nucleus
* Element: all atoms with the same atomic number are the same element (e.g. all Hydrogen nuclei have 1 proton, all Carbon atoms have 6 protons, etc)
* Isotope: all atoms with the same atomic number and the same atomic mass are the same isotope. There are several isotopes of most elements. For instance, Carbon nuclei will always have 6 protons, but a Carbon-12 nucleus will have 6 neutrons, and Carbon-13 will have 7 neutrons. carbon-12 and Carbon-13 are examples of isotopes of Carbon.
* Isomer: for two nuclei to be the same isomer, they must have the same atomic number and atomic mass, and be in the same energy state.

#### Energy States

For a given isotope, there will be a number of discrete energy levels. Each nucleus of that isotope will exist in one of these energy states. These energy states are labelled such that state 0 is the lowest energy state, state 1 is the second lowest and so on. The energy difference between energy states is typically defined in units of keV (1keV = $1.6\times 10 ^{-16}$ J). If it isn't stated which energy state an isomer is, it is very likely the ground state which is being referred to.

### Nuclear Decay

Many isomers are unstable and will decay to a lower energy isomer. This decay will emit one or more particles from the nucleus and may also emit some radiation. Dependent on which particle is emitted, the composition of the nucleus will change accordingly. A table below shows common types of particle which may be emitted and the change this causes to the structure of a nucleus.

| Decay Type      | Change to Atomic Number | Change to Atomic Mass |
| ----------- | ----------- | -- |
| Alpha Emission  ( $\alpha$ ) | -4  | -2 |
| Electron emission ( $\beta^{-}$ )     | +1  | 0  |
| Gamma Emission  ( $\gamma$ ) | 0  | 0 |
| Electron capture  ( $\epsilon$ ) | 0  | -1 |


For each individual nuclei, it cannot be predicted exactly when it will decay. However, we may observe a large colelction of isomers measure the timescales over which they decay occurs and observe which particles are emitted. Xenon-135 (written as Xe $^{135}$ ) decays via electron emission. Xenon has an atomic number of 54 so, consulting the table above, we see that it will turn into a nucleus with an atomic number of 55 and its atomic mass will remain unchanged at 135. This means a nucleus of Xe $^{135}$ will decay to form a nucleus of Cs $^{135}$ . 

We observe that, given a large sample of Xe $^{135}$ , half of the nuclei will have decayed to Cs $^{135}$ after 9.14 hours. As the number of Xe $^{135}$ nuceli that decay each second is proprotional to the number of Xe $^{135}$ nuclei present, we may write equations which describe how the number of both Xe $^{135}$ and Cs $^{135}$ change over time due to this decay:

$$ \eqalign{
\frac{\mathrm{d}n_{Xe135}}{\mathrm{d}t} = - \lambda_{Xe135} n_{Xe135},\\
\frac{\mathrm{d}n_{Cs135}}{\mathrm{d}t} = \lambda_{Xe135} n_{Xe135},
}
$$

where $n_{Xe135}$ is the nubmer of moles of Xe $^{135}$ present, $n_{Cs135}$ is the number of moles of Cs $^{135}$ present, $t$ is time and \lambda_{Xe135} is the decay rate of Xe $^{135}$ . For a given isomer, we may obtain its decay rate $\lambda$ from its half-life $t_{\frac{1}{2}}$ using the following equation:

$$
\lambda = \frac{\ln{2}}{t_{\frac{1}{2}}}.
$$

Note that the decay constant has units of s $^{-1}$ so the half-life should be converted into seconds before this calculation takes place. So, for Xe $^{135}$ , we get:

$$
\lambda_{Xe135} = \frac{0.6931}{9.14\mathrm{h} \times 3600\mathrm{sh}^{-1}} = 2.1065 \times 10 ^{-5} \mathrm{s}^{-1}.
$$

This means that, form every million nuclei of Xe $^{135}$ present, around 21 of them will decay each second.

We can return the differential equations we defined earlier for the rate of change of the number of moles of Xe $^{135}$ and Cs $^{135}$ and solve these by a number of differen means to describe the number of moles of these two isotopes over a period of time. We can plot the number of moles of the isotopes present as a function of time giving an initial population of 1 mole of Xe $^{135}$ :


