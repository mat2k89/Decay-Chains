# Decay Chains

## Background

So far, we have dealt with the case where one isomer decays to another and this resulting isomer is stable. However, sometimes the resulting isomer isomer can also be radioactive and so decay to another isomer and so on. There are some complex decay chains, such as the [Thorium decay series](https://en.wikipedia.org/wiki/Decay_chain#Thorium_series), which can include branching. However, we'll stick to a simpe one for now. Co $^{65}$ deacys via beta decay to Ni $^{65}$ which, in turn, decays via beta decay to Cu $^{65}$, which is stable.

## Constructing a Decay Chain using ENDF

We may use the ENDF dataset to construct a dataseries. For instance, if we examine ```dec-027_Co_065.endf``` we find Co $^{65}$ decays via beta decay with a half-life of 1.16s (and so a decay rate of 0.596/s). Because it beta decays, we know it will change into a new isomer with the same atomic mass but an atomic number one higher. Nickel has an atomic number one higher than Cobalt, so we know it will decay to Ni $^{65}$. We may then examine ```dec-028_Ni_065.endf``` to find it decays via beta dcay with a half-life of 2.52hours (and so a decay rate of 7.65 $\times 10^{-5}$ /s). Because it decays via beta decay, we know it will change into a new isomer with the same atomic mass but an atomic number one higher. Copper has an atomic mass one higher than Nickel, so we know it will decay to Cu $^{65}$. When we examine ```dec-029_Cu_065``` we see that this isomer is stable so we know this is the end of the decay chain. This means we may construct the following system of equations to describe a group of isomers containing purely Co $^{65}$:

$$ \eqalign{
\frac{\mathrm{d}n_{Co65}}{\mathrm{d}t} &= - \lambda_{Co65} n_{Co65},\\
\frac{\mathrm{d}n_{Ni65}}{\mathrm{d}t} &= \lambda_{Co65} n_{Co65} n_{Co65} - \lambda_{Ni65} n_{Ni65},\\
\frac{\mathrm{d}n_{Cu65}}{\mathrm{d}t} &=  \lambda_{Ni65} n_{Ni65},
}
$$

where $n_{Co65}$ is the number of moles of Co $^{65}$ present, $n_{Ni65}$ is the number of moles of Ni $^{65}$ present, $n_{Cu65}$ is the number of moles of Cu $^{65}$ present, $t$ is time, \lambda_{Co65} is the decay rate of Co $^{65}$, and $\lambda_{Ni65}$ is the decay rate of NI $^{65}$ .

## Activity 2

Write a piece of code which receives the name of an isotope (e.g. ```Co65```), the number of moles of this isotope present at $t$ =0 and a set of output times (you may assume the first output time is always 0s). Your code should calculate the number of moles of this isomer and any isomers created as part of this isomer's decay chain at the specified output times. 

Tests are provided for this activity - edit the relevat functions in ```test_interfaces.py``` to make sure they can interact with you code. It is recommended that you use the data structuresa nd methods you think are best suited to solve the problem to produce your code, then extract the relevant data in ```test_interfaces.py```, rather than letting the format of the funcitons in ```test_interfaces.py``` dictate how you structure your code.

Tip: You should be able to adapt the code produced in Activity 1 to produce this code. When adapting the code, it would be sensible to ake sure the tests from Activity 1 are still applied to your code, to ensure any changes you make do not break your code. This may require editing the parts of the file ```test_interfaces.py``` relatig to Activity 1.

Tip 2: You will need to decide how to read the relevant files to obtain the necessary data and how to construct and solve the resultat equations.
