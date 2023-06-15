# Decay Chains

## Background

So far, we have dealt with the case where one isomer decays to another and this resulting isomer is stable. However, sometimes the resulting isomer isomer can also be radioactive and so decay to another isomer and so on. There are some complex decay chains, such as the [Thorium decay series](https://en.wikipedia.org/wiki/Decay_chain#Thorium_series), which can include branching. However, we'll stick to a simpe one for now. Co$^{65}$ deacys via beta decay to Ni$^{65}$ which, in turn, decays via beta decay to Cu$^{65}$, which is stable.

## Constructing a Decay Chain using ENDF

We may use the ENDF dataset to construct a dataseries. For instance, if we examine ```dec-027_Co_065.endf``` we find Co$^{65}$ decays via beta decay with a half-life of 1.16s (and so a decay rate of 0.596/s). Because it beta decays, we know it will change into a new isomer with the same atomic mass but an atomic number one higher. Nickel has an atomic number one higher than Cobalt, so we know it will decay to Ni$^{65}$. We may then examine ```dec-028_Ni_065.endf``` to find it decays via beta dcay with a half-life of 2.52hours (and so a decay rate of 7.65$\times 10^{-5}$/s). Because it decays via beta decay, we know it will change into a new isomer with the same atomic mass but an atomic number one higher. Copper has an atomic mass one higher than Nickel, so we know it will decay to Cu$^{65}$. When we examine ```dec-029_Cu_065``` we see that this isomer is stable so we know this is the end of the decay chain.
